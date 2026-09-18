# VSR Digital Hub

A full website for **VSR Digital Hub** with:

- A dark, animated marketing site (hero, stats, about, services, process, benefits, FAQ, contact)
- Customer accounts (register / log in / log out)
- A private customer dashboard where logged-in users can view their profile and raise service requests
- A Django admin panel to manage users, services, contact messages, and requests
- **MySQL** as the database, **Django** as the backend — every file is plain Python, HTML, and CSS (no Node/React build step)

---

## 1. Requirements

- Python 3.10+
- MySQL Server 8+ running locally (or a remote MySQL instance)
- pip

---

## 2. Set up MySQL

Log into MySQL and create the database:

```sql
CREATE DATABASE vsr_digital_hub CHARACTER SET utf8mb4;
CREATE USER 'vsr_user'@'localhost' IDENTIFIED BY 'your-password';
GRANT ALL PRIVILEGES ON vsr_digital_hub.* TO 'vsr_user'@'localhost';
FLUSH PRIVILEGES;
```

You can also just use your existing `root` user — see `.env` below.

---

## 3. Project setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env
# then edit .env with your real MySQL username/password

# 4. Create the database tables (this also seeds the 6 default services)
python manage.py migrate

# 5. Create an admin account (for /admin/)
python manage.py createsuperuser

# 6. Run the site
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** for the site and
**http://127.0.0.1:8000/admin/** for the admin panel.

> This project uses **PyMySQL** (a pure-Python MySQL driver) instead of
> `mysqlclient`, so there's nothing to compile — `pip install` is enough,
> even on machines without MySQL's C headers.

---

## 4. Project structure

```
vsr_digital_hub/
├── manage.py                  # Django's command-line entry point
├── requirements.txt
├── .env.example                # Copy to .env and fill in real values
├── vsr_project/                 # Project-level settings
│   ├── settings.py              # MySQL config, installed apps, etc.
│   ├── urls.py                  # Root URL routing
│   ├── wsgi.py / asgi.py
├── core/                        # The main (and only) app
│   ├── models.py                # CustomUser, Service, ContactMessage, ServiceInquiry
│   ├── views.py                 # home, signup, login, dashboard, profile
│   ├── forms.py                 # SignUpForm, LoginForm, ContactForm, etc.
│   ├── admin.py                 # Registers all models in /admin/
│   ├── urls.py                  # App-level routes
│   ├── migrations/               # Database schema history (incl. seed data)
│   ├── templates/core/           # All HTML pages
│   └── static/core/              # CSS + logo image
```

---

## 5. How the login system works

- Accounts use Django's built-in authentication system, extended with a
  `CustomUser` model (`core/models.py`) that adds `phone_number`,
  `company_name`, and `address`.
- Passwords are **never stored in plain text** — Django hashes them
  (PBKDF2 by default) before writing to MySQL.
- `/accounts/register/` creates a new row in the `core_customuser` MySQL
  table and logs the user in immediately.
- `/accounts/login/` checks the submitted password against the stored
  hash.
- `/dashboard/` is protected with `@login_required` — visiting it while
  logged out redirects to the login page.
- Every request a customer submits from their dashboard is saved to the
  `core_serviceinquiry` table, linked to their account, and shown back
  to them on their next visit.

---

## 6. Managing content

Everything editable — the services shown on the homepage, contact
messages received, and customer service requests — is manageable from
the Django admin at `/admin/` once you've created a superuser.

---

## 7. Going to production

Before deploying:

- Set `DJANGO_DEBUG=False` and a real, secret `DJANGO_SECRET_KEY` in `.env`
- Set `DJANGO_ALLOWED_HOSTS` to your real domain
- Run `python manage.py collectstatic` and serve `/static/` with your
  web server (e.g. Nginx) or a tool like WhiteNoise
- Use a production server such as **gunicorn** or **uwsgi** behind Nginx
  instead of `manage.py runserver`
- Point `DB_HOST` / `DB_PORT` at your production MySQL instance
