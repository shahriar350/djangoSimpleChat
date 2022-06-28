from django.urls import path
from . import views

urlpatterns = [
    path("", views.ChatTemplate.as_view())
]
