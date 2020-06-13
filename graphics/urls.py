from django.urls import path, include
from .views import (
    AnimatedCreaturesListView, 
    AnimatedObjectsListView, 
    LandscapeListView,
    DetailView,
    OrderItemView
)
from . import views


urlpatterns = [
    path('creatures/', AnimatedCreaturesListView.as_view(), name='creatures' ),
    path('detail/<pk_free>/', DetailView.as_view(), name='detail' ),
    path('objects/', AnimatedObjectsListView.as_view(), name='objects' ),
    path('landscapes/', LandscapeListView.as_view(), name='landscapes' ),
    path('order/', OrderItemView.as_view(), name='order-item'),
    path('search/', include('search.urls')),
]