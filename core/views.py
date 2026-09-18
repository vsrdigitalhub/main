from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import ContactForm, LoginForm, ProfileUpdateForm, ServiceInquiryForm, SignUpForm
from .models import Service, ServiceInquiry


def home(request):
    """
    Public landing page. Renders the services pulled from MySQL and
    handles the contact form submission (saved to MySQL too).
    """
    services = Service.objects.all()
    contact_form = ContactForm()

    if request.method == "POST" and "message" in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_message = contact_form.save(commit=False)
            if request.user.is_authenticated:
                contact_message.user = request.user
            contact_message.save()
            messages.success(request, "Thanks! Your message has been sent — we'll be in touch soon.")
            return redirect("home")

    context = {
        "services": services,
        "contact_form": contact_form,
    }
    return render(request, "core/index.html", context)


class VSRLoginView(LoginView):
    """Customer login. Django checks the hashed password stored in MySQL."""
    template_name = "core/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("dashboard")


def signup(request):
    """Create a new customer account, written to the MySQL user table."""
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to VSR Digital Hub, {user.username}!")
            return redirect("dashboard")
    else:
        form = SignUpForm()

    return render(request, "core/register.html", {"form": form})


@login_required
def dashboard(request):
    """
    Customer panel. Only reachable when the user is logged in
    (login_required redirects to the login page otherwise). Shows the
    account details and service inquiries pulled straight from MySQL
    for the logged-in user.
    """
    inquiry_form = ServiceInquiryForm()

    if request.method == "POST":
        inquiry_form = ServiceInquiryForm(request.POST)
        if inquiry_form.is_valid():
            inquiry = inquiry_form.save(commit=False)
            inquiry.user = request.user
            inquiry.save()
            messages.success(request, "Your request has been submitted.")
            return redirect("dashboard")

    inquiries = ServiceInquiry.objects.filter(user=request.user)

    context = {
        "inquiries": inquiries,
        "inquiry_form": inquiry_form,
    }
    return render(request, "core/dashboard.html", context)


@login_required
def profile_update(request):
    """Lets a logged-in customer edit the profile fields stored in MySQL."""
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("dashboard")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "core/profile.html", {"form": form})
