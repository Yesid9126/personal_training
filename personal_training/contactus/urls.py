from django.urls import path

# Views
from personal_training.contactus.views import views as contactus_views

app_name = "contactus"
urlpatterns = [
    path(route="", view=contactus_views.ContactUsView.as_view(), name="contactus"),
]
