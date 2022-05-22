from django.urls import path
from tangle import views

urlpatterns = [
    path("", views.home, name="home"),
]
