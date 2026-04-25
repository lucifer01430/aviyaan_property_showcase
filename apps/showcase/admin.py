from django.contrib import admin
from django.utils.html import format_html
from .models import Segment, SegmentMedia


class SegmentMediaInline(admin.TabularInline):
    model = SegmentMedia
    extra = 1
    fields = (
        'preview',
        'title',
        'media_type',
        'image',
        'video_source',
        'video_file',
        'video_url',
        'thumbnail',
        'display_order',
        'is_active',
    )
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        if obj.thumbnail:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit:cover;border-radius:6px;" />',
                obj.thumbnail.url
            )
        return "No Preview"

    preview.short_description = "Preview"


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = (
        'cover_preview',
        'title',
        'slug',
        'display_order',
        'is_active',
        'created_at',
    )
    list_editable = ('display_order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug')
    list_filter = ('is_active', 'created_at')
    inlines = [SegmentMediaInline]

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" width="90" height="65" style="object-fit:cover;border-radius:6px;" />',
                obj.cover_image.url
            )
        return "No Image"

    cover_preview.short_description = "Cover"


@admin.register(SegmentMedia)
class SegmentMediaAdmin(admin.ModelAdmin):
    list_display = (
        'preview',
        'segment',
        'title',
        'media_type',
        'display_order',
        'is_active',
        'created_at',
    )
    list_editable = ('display_order', 'is_active')
    list_filter = ('media_type', 'is_active', 'segment')
    search_fields = ('segment__title', 'title')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="90" height="65" style="object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        if obj.thumbnail:
            return format_html(
                '<img src="{}" width="90" height="65" style="object-fit:cover;border-radius:6px;" />',
                obj.thumbnail.url
            )
        return "No Preview"

    preview.short_description = "Preview"