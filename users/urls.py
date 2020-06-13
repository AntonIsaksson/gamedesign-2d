from django.urls import path

from .views import (
    MembershipSelectView, 
    PaymentView, 
    updateTransactionRecords,
    account_view,
    cancelSubscription
)

app_name = 'users'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', updateTransactionRecords, name='update-transactions'),
    path('cancel/', cancelSubscription, name='cancel')
]