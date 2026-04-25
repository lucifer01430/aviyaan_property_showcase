from django.shortcuts import get_object_or_404, redirect, render

from .models import Segment


def showcase_home(request):
    return redirect('core:home')


def segment_detail(request, slug):
    segment = get_object_or_404(Segment, slug=slug, is_active=True)

    media_items = segment.media_items.filter(is_active=True).order_by('display_order', 'id')
    images = media_items.filter(media_type='image')
    videos = media_items.filter(media_type='video')

    return render(request, 'showcase/segment_detail.html', {
        'segment': segment,
        'images': images,
        'videos': videos,
        'media_items': media_items,
    })
