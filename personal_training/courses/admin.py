# Dajngo
from django.contrib import admin

# Models
from personal_training.courses.models.models import Course, Content


class ContentCourseInLine(admin.TabularInline):
    model = Content
    autocomplete_fields = ["course"]
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ["name", "slug_name"]
    list_display = ["name", "slug_name", "course_type"]
    list_filter = ["course_type", ]
    inlines = [ContentCourseInLine]

@admin.register(Content)
class ContentCourse(admin.ModelAdmin):
    search_fields = ["name", "slug_name"]
    list_display = ["name", "slug_name",]
    list_filter = ["name", "slug_name", ]

