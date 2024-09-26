from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_url/', views.get_url, name='get_url' )
]
