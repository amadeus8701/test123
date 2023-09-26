from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('detectme', views.detectme, name='detectme'),
    path('video_feed/<int:stream_id>/', views.video_feed, name='video_feed'),
]