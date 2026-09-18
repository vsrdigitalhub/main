from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Customer / user account for VSR Digital Hub.

    Extends Django's built-in auth user so login, password hashing,
    sessions, and the admin panel all work out of the box, while adding
    the extra profile fields VSR needs. All rows are stored in the
    MySQL database configured in settings.py.
    """

    phone_number = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=255, blank=True)
    is_customer = models.BooleanField(
        default=True,
        help_text="Marks this account as a VSR Digital Hub customer.",
    )
    date_joined_hub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Service(models.Model):
    """A service VSR Digital Hub offers, shown on the homepage."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon = models.CharField(
        max_length=50,
        default="cube",
        help_text="Name of the icon rendered in the service card.",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """
    A message submitted through the public contact form.

    Saved to MySQL so the VSR team can follow up. If the visitor was
    logged in, the account is linked automatically.
    """

    user = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="messages",
    )
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'General enquiry'}"


class ServiceInquiry(models.Model):
    """
    A request a logged-in customer raises from their dashboard, e.g.
    "start a Web Development project". Lets the customer panel show a
    real, personal history that is backed by MySQL rather than being
    static content.
    """

    STATUS_CHOICES = [
        ("new", "New"),
        ("in_review", "In review"),
        ("in_progress", "In progress"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="inquiries"
    )
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True
    )
    details = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Service inquiries"

    def __str__(self):
        return f"{self.user.username} - {self.service}"
