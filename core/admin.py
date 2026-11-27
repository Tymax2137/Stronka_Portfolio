from django.contrib import admin
from .models import ProfileInfo, Project, ProjectImage

admin.site.register(ProfileInfo)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_published", "created_at")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]