from django.db import models
from django.utils.text import slugify


class Segment(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='segments/covers/')
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Segment.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class SegmentMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    VIDEO_SOURCE_CHOICES = (
        ('file', 'File Upload'),
        ('url', 'External URL'),
    )

    segment = models.ForeignKey(
        Segment,
        on_delete=models.CASCADE,
        related_name='media_items'
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    image = models.ImageField(upload_to='gallery/images/', blank=True, null=True)
    video_file = models.FileField(upload_to='videos/files/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    video_source = models.CharField(
        max_length=10,
        choices=VIDEO_SOURCE_CHOICES,
        default='file',
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', 'id']

    def __str__(self):
        if self.title:
            return f"{self.segment.title} - {self.title}"
        return f"{self.segment.title} - {self.media_type}"

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.media_type == 'image':
            if not self.image:
                raise ValidationError("For image type, image is required.")
        elif self.media_type == 'video':
            if self.video_source == 'file' and not self.video_file:
                raise ValidationError("For video file type, video_file is required.")
            if self.video_source == 'url' and not self.video_url:
                raise ValidationError("For video URL type, video_url is required.")