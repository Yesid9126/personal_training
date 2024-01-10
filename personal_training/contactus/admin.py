# Dajngo
from django.contrib import admin

# Models
from personal_training.contactus.models.models import Contacts, ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["pk", "title1", "description1", "title2", "title3"]


# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ["pk", "address", "latitude", "longitude"]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "email", "phone"]
