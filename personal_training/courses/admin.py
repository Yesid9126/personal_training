# Dajngo
from django.contrib import admin

# Models
from personal_training.courses.models.models import AttachFile, Class, Course


class ClassCourseInLine(admin.StackedInline):
    model = Class
    autocomplete_fields = ["course"]
    extra = 0
    readonly_fields = ["slug_name", "my_video_thumbnail", "my_video_url_thumbnail"]
    show_change_link = True


class AttachFileClassInLine(admin.StackedInline):
    model = AttachFile
    autocomplete_fields = ["cource_class"]
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ["name", "slug_name"]
    list_display = ["name", "slug_name", "course_type", "created"]
    list_display_links = ["name"]
    list_filter = [
        "course_type",
    ]
    autocomplete_fields = ["tags"]
    readonly_fields = ["slug_name", "my_image_thumbnail"]

    inlines = [ClassCourseInLine]

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.image.delete()
        return super().delete_queryset(request, queryset)


@admin.register(Class)
class ClassCourse(admin.ModelAdmin):
    search_fields = ["name", "slug_name"]
    list_display = [
        "name",
        "slug_name",
    ]
    list_filter = [
        "course",
    ]
    readonly_fields = ["slug_name", "my_video_thumbnail", "my_video_url_thumbnail"]
    inlines = [AttachFileClassInLine]


@admin.register(AttachFile)
class AttachFileCourse(admin.ModelAdmin):
    search_fields = ["name", "slug_name"]
    list_display = [
        "name",
        "slug_name",
    ]
