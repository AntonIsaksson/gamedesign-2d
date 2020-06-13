from django.urls import path, include
from .views import (
    AnimatedCreaturesListView, 
    AnimatedObjectsListView, 
    LandscapeListView,
    CreatureDetailView,
    CreatureDetailViewPremium,
    ObjectDetailView,
    ObjectDetailViewPremium,
    LandscapeDetailView,
    LandscapeDetailViewPremium, 
    OrderItemView
)
from . import views


urlpatterns = [
    path('creatures/', AnimatedCreaturesListView.as_view(), name='creatures' ),
    path('creatures/<pk_free>/', CreatureDetailView.as_view(), name='creature-detail' ),
    path('creatures/premium/<int:pk>/', CreatureDetailViewPremium.as_view(), name='creature-detail-premium' ),
    path('objects/', AnimatedObjectsListView.as_view(), name='objects' ),
    path('objects/<int:pk>/', ObjectDetailView.as_view(), name='object-detail' ),
    path('objects/premium/<int:pk>/', ObjectDetailView.as_view(), name='object-detail-premium' ),
    path('landscapes/', LandscapeListView.as_view(), name='landscapes' ),
    path('landscapes/<int:pk>/', LandscapeDetailView.as_view(), name='landscape-detail' ),
    path('landscapes/premium/<int:pk>/', LandscapeDetailView.as_view(), name='landscape-detail-premium' ),
    path('order/', OrderItemView.as_view(), name='order-item'),
    path('search/', include('search.urls')),
]