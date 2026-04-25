from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, default="Aviyaan Showcase")
    site_tagline = models.CharField(max_length=255, blank=True, null=True)
    hero_title = models.CharField(max_length=255, blank=True, null=True)
    hero_subtitle = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='site/logo/', blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    footer_text = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name