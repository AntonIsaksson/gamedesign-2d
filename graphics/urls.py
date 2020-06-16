from django.urls import path, include
from .views import (
    AnimatedCreaturesListView,
    AllCreaturesListView,
    AnimatedObjectsListView, 
    AllObjectsListView,
    LandscapeListView,
    AllLandscapesListView,
    DetailView,
    LatestItemsListView,
    OrderItemView
)
from . import views


urlpatterns = [
    path('creatures/', AnimatedCreaturesListView.as_view(), name='creatures' ),
    path('creatures/all', AllCreaturesListView.as_view(), name='creatures-all' ),
    
    path('objects/', AnimatedObjectsListView.as_view(), name='objects' ),
    path('objects/all', AllObjectsListView.as_view(), name='objects-all' ),

    path('landscapes/', LandscapeListView.as_view(), name='landscapes' ),
    path('landscapes/all', AllLandscapesListView.as_view(), name='landscapes-all' ),

    path('detail/<pk_free>/', DetailView.as_view(), name='detail' ),
    path('order/', OrderItemView.as_view(), name='order-item'),
    path('latest/', LatestItemsListView.as_view(), name='latest'),
    path('search/', include('search.urls')),
]