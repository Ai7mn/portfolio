from django.contrib import admin
from .models import Project, ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "visible",
        "local",
        "display_order",
        "timeStamp",
    )
    list_filter = ("category", "visible", "local")
    search_fields = ("name", "category")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("display_order",)


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "timeStamp")
    list_filter = ("project",)
    search_fields = ("title", "description")
