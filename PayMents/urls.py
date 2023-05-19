from .views import PaymentView
from django.urls import path

urlpatterns = [
    path('payment/', PaymentView.as_view())
]
