from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dayroom-home'),
    path('about/', views.about, name='dayroom-about'),
]
