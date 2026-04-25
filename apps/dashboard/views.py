from django.shortcuts import render
from apps.showcase.models import Segment, SegmentMedia


def dashboard_home(request):
    context = {
        'total_segments': Segment.objects.count(),
        'active_segments': Segment.objects.filter(is_active=True).count(),
        'total_media': SegmentMedia.objects.count(),
        'active_media': SegmentMedia.objects.filter(is_active=True).count(),
    }
    return render(request, 'dashboard/dashboard_home.html', context)