from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mh-home'),
    path('about/', views.about, name='mh-about'),
    path('overview/', views.overview, name='mh-overview'),
]