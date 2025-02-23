from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from PIL import Image
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    subtitle = models.CharField(max_length=200, default='Made with Love')
    banner_image = models.ImageField(upload_to='projects/thumbnails_banner/', blank=True, null=True)
    description = RichTextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    small_description = RichTextField()
    thumbnail_image = models.ImageField(upload_to='projects/thumbnails/', blank=True, null=True)
    # The "carousel_images" field is removed as it's now handled by a related model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    def clean(self):
        """
        Override the clean method to validate image size before saving.
        """
        if self.thumbnail_image:
            img = Image.open(self.thumbnail_image)
            width, height = img.size
            if width != 1939 or height != 1572:
                raise ValidationError("Thumbnail image must be 1939x1572 pixels.")
            
        if self.banner_image:
            img = Image.open(self.banner_image)
            width, height = img.size
            if width != 1290 or height != 560:
                raise ValidationError("Banner image must be 1290x560 pixels.")
            
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not set
            self.slug = slugify(self.title)
        else:  # Ensure uniqueness
            original_slug = self.slug
            counter = 1
            while Project.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='carousel_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/carousel/', blank=True, null=True)
    # Optional: You can add order field to manage the image sequence
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Image for {self.project.title} - {self.order}"

    class Meta:
        ordering = ['order']
