from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'logo_preview', 'contact_number', 'contact_email', 'updated_at')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit:contain;" />',
                obj.logo.url
            )
        return "No Logo"

    logo_preview.short_description = "Logo"