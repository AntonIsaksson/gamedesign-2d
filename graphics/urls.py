from django.urls import path
from .views import AnimatedCreaturesListView, AnimatedObjectsListView, LandscapeListView
from . import views

urlpatterns = [
    path('creatures/', AnimatedCreaturesListView.as_view(), name='creatures' ),
    path('objects/', AnimatedObjectsListView.as_view(), name='objects' ),
    path('landscapes/', LandscapeListView.as_view(), name='landscapes' ),
]