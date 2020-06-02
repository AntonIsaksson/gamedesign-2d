from django.urls import path
from .views import (
    AnimatedCreaturesListView, 
    AnimatedObjectsListView, 
    LandscapeListView,
    CreatureDetailView,
    ObjectDetailView,
    LandscapeDetailView
)
from . import views

urlpatterns = [
    path('creatures/', AnimatedCreaturesListView.as_view(), name='creatures' ),
    path('creatures/<int:pk>/', CreatureDetailView.as_view(), name='creature-detail' ),
    path('objects/', AnimatedObjectsListView.as_view(), name='objects' ),
    path('objects/<int:pk>/', ObjectDetailView.as_view(), name='object-detail' ),
    path('landscapes/', LandscapeListView.as_view(), name='landscapes' ),
    path('landscapes/<int:pk>/', LandscapeDetailView.as_view(), name='landscape-detail' ),
]