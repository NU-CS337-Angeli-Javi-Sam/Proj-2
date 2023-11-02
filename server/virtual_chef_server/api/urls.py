from django.urls import path
from . import views

urlpatterns = [
    path('receive-url/', views.receive_url, name='receive_url'),
]
