# Django
from django.urls import path

# Views
from personal_training.users import views as user_views

app_name = "users"
urlpatterns = [
    path(route="signup", view=user_views.SignUpView.as_view(), name="signup"),
]
