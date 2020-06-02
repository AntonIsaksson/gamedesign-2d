from django.urls import path, include
from .views import home
from graphics.views import HomeListViewCreature, HomeListViewLandscape, HomeListViewObject
from . import views

urlpatterns = [
    path('', HomeListViewCreature.as_view(), name='home-page'),
    path('', HomeListViewObject.as_view(), name='home-page'),
    path('', HomeListViewLandscape.as_view(), name='home-page'),
]
#Change these URLs later