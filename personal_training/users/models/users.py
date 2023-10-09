from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for personal training.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    """User model.

    Extend from Django abstract user, change the username field to email
    and add some extra info
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist',
        }
    )
    phone_number = models.CharField(max_length=17, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
    )
    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='set to true when address email have verified'
    )

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email
