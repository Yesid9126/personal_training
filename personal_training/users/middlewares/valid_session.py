from django.shortcuts import redirect
from django.urls import reverse


class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not (
            request.path == reverse("users:login")
            or request.path == reverse("users:signup")
            or "password" in request.path
            or "users" not in request.path
        ):
            # User is not authenticated, redirect to login page
            return redirect(reverse("users:login"))  # Assuming your login URL name is 'login'
        elif request.user.is_authenticated and (
            request.path
            in [
                reverse("users:login"),
                reverse("users:signup"),
            ]
            or "password" in request.path
        ):
            # User is already authenticated, redirect to another page (e.g., home)
            return redirect(reverse("home:index"))  # Assuming your home URL name is 'home'
        return self.get_response(request)
