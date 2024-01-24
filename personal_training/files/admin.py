# # Dajngo
# from django.contrib import admin

# # Models
# from personal_training.files.models.models import File, Folder


# class FileInLine(admin.TabularInline):
#     model = File
#     autocomplete_fields = ["folder"]
#     extra = 0
#     readonly_fields = ["slug_name", "my_source_thumbnail"]


# @admin.register(Folder)
# class FolderAdmin(admin.ModelAdmin):
#     search_fields = ["name", "slug_name"]
#     list_display = ["name", "slug_name"]
#     readonly_fields = ["slug_name"]
#     inlines = [FileInLine]


# @admin.register(File)
# class FileCourse(admin.ModelAdmin):
#     search_fields = ["name", "folder", "slug_name"]
#     list_display = [
#         "name",
#         "folder",
#         "slug_name",
#     ]
#     list_filter = [
#         "folder__name",
#     ]
#     readonly_fields = ["slug_name", "my_source_thumbnail"]

#     # def folder(self, obj):
#     #     return obj.folder.name
