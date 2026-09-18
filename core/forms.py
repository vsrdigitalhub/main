from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import ContactMessage, CustomUser, ServiceInquiry


class LoginForm(AuthenticationForm):
    """Styled login form. Django validates the password hash stored in MySQL."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-input", "placeholder": "Username", "autofocus": True,
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-input", "placeholder": "Password",
        })


class SignUpForm(UserCreationForm):
    """
    Registration form for new VSR Digital Hub customers.

    On save, Django hashes the password and writes a new row to the
    MySQL-backed CustomUser table.
    """

    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    company_name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "phone_number",
            "company_name",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "username": "Choose a username",
            "email": "you@example.com",
            "phone_number": "+91 98765 43210",
            "company_name": "Your company (optional)",
            "password1": "Create a password",
            "password2": "Confirm password",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-input",
                "placeholder": placeholders.get(field_name, ""),
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data.get("phone_number", "")
        user.company_name = self.cleaned_data.get("company_name", "")
        if commit:
            user.save()
        return user


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone_number", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-input", "placeholder": "Your email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-input", "placeholder": "Phone number"}),
            "subject": forms.TextInput(attrs={"class": "form-input", "placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"class": "form-input", "placeholder": "Tell us about your project", "rows": 4}),
        }


class ServiceInquiryForm(forms.ModelForm):
    class Meta:
        model = ServiceInquiry
        fields = ["service", "details"]
        widgets = {
            "service": forms.Select(attrs={"class": "form-input"}),
            "details": forms.Textarea(attrs={"class": "form-input", "placeholder": "Describe what you need", "rows": 3}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number", "company_name", "address"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"}),
            "email": forms.EmailInput(attrs={"class": "form-input"}),
            "phone_number": forms.TextInput(attrs={"class": "form-input"}),
            "company_name": forms.TextInput(attrs={"class": "form-input"}),
            "address": forms.TextInput(attrs={"class": "form-input"}),
        }
