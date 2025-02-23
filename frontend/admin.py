from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty forms to display by default
    fields = ('image', 'order')  # You can add more fields if necessary
    ordering = ['order']  # Ensure images are ordered by the "order" field

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'tech_stack', 'created_at', 'updated_at', 'project_url', 'is_featured')  # Add is_featured to the list display
    search_fields = ('title', 'subtitle', 'tech_stack')
    list_filter = ('created_at', 'updated_at', 'is_featured')  # Filter by is_featured
    list_editable = ('tech_stack', 'is_featured')  # Make is_featured editable in the list view
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'banner_image', 'description', 'tech_stack', 'project_url', 'video_url', 'small_description', 'thumbnail_image', 'is_featured')
        }),
        ('Carousel Images', {
            'fields': (),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': (),  # Leave this empty because created_at and updated_at are auto-managed
            'classes': ('collapse',)
        }),
    )
    inlines = [ProjectImageInline]  # Add the inline for ProjectImage

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].required = True
        form.base_fields['description'].required = True
        return form

admin.site.register(Project, ProjectAdmin)
