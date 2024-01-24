from django.urls import path

# Views
from personal_training.courses.views import views as courses_views

app_name = "courses"
urlpatterns = [
    path(route="", view=courses_views.CoursesView.as_view(), name="list"),
]
