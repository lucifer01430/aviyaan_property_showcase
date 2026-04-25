from django.shortcuts import render

from apps.showcase.models import Segment


def home(request):
    segments = Segment.objects.filter(is_active=True).order_by('display_order', 'title')

    return render(request, 'core/home.html', {
        'segments': segments,
        'featured_segment': segments.first(),
        'curated_segments': segments[:3],
    })
