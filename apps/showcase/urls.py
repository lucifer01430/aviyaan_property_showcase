from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    path('', views.showcase_home, name='showcase_home'),
    path('<slug:slug>/', views.segment_detail, name='segment_detail'),
]