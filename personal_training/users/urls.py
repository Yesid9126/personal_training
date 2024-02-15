# Django
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView

# Views
from personal_training.users import views as user_views
from personal_training.users.api.views import update_cart

app_name = "users"
urlpatterns = [
    path(route="signup/", view=user_views.SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("my-account/", TemplateView.as_view(template_name="users/my-account.html"), name="my_account"),
    path(
        "password_reset/",
        PasswordResetView.as_view(success_url=reverse_lazy("users:password_reset_done")),
        name="password_reset",
    ),
    path("password_reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("update-cart/", update_cart, name="update_cart"),
    path("cart/", user_views.CartView.as_view(), name="cart"),
]
