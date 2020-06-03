from django.urls import path, include
from .views import home
# from graphics.views import HomeListViewCreature, HomeListViewLandscape, HomeListViewObject
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
]
#Change these URLs later