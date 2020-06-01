from django.urls import path
from .views import AnimatedCreaturesListView
from . import views

urlpatterns = [
    path('creatures/', AnimatedCreaturesListView.as_view(), name='creatures' ),
]