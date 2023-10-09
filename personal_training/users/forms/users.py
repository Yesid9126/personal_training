"""Users Forms"""

# Django
from django import forms

# Models
from personal_training.users.models.users import User


class SignUpForm(forms.Form):
    """Sign up form."""

    password = forms.CharField(
        max_length=70,
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirmation = forms.CharField(
        max_length=70,
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone_number = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        initial='+57',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo +57 300 000 00 00'}))

    email = forms.CharField(
        min_length=6,
        max_length=70,
        label='',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'})
    )

    def clean_phone_number(self):
        """Phone number must be unique."""
        phone_number = self.cleaned_data['phone_number']
        phone_number_taken = User.objects.filter(phone_number=phone_number).exists()
        if phone_number_taken:
            raise forms.ValidationError('Número de teléfono ya registrado.')
        return phone_number

    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email ya registrado.')
        return email

    def clean(self):
        """Veirify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        data['username'] = data['email']
        user = User.objects.create_user(**data)
        return user
