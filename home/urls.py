from django.urls import path, include
from .views import home
from graphics.views import HomeListView
from . import views

urlpatterns = [
    path('', HomeListView.as_view(), name='home-page'),
]