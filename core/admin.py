from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "project_type", "category", "display_order")
    list_filter = ("project_type",)
    list_editable = ("display_order",)
    search_fields = ("title", "category")
    ordering = ("display_order", "id")
