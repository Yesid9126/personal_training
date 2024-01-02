from django.urls import path

# Views
from personal_training.home.views import views as home_views

app_name = "home"
urlpatterns = [
    path(route="home/", view=home_views.HomeView.as_view(), name="index"),
]
