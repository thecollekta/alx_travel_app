# listings/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"listings", views.ListingViewSet)
router.register(r"bookings", views.BookingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
