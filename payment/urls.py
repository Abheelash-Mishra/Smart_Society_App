from django.urls import path
from .views import Payment, Portal, Success

urlpatterns = [
    path("", Payment.as_view(), name="payment"),
    path("portal/", Portal.as_view(), name="portal"),
    path("portal/success", Success.as_view(), name="success"),
]