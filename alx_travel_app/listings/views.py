# listings/views.py

from rest_framework import viewsets

from .models import Booking, Listing
from .serializers import BookingSerializer, ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by("-created_at")
    serializer_class = ListingSerializer
    lookup_field = "id"


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by("-created_at")
    serializer_class = BookingSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = super().get_queryset()
        listing_id = self.request.query_params.get("listing_id")
        if listing_id:
            queryset = queryset.filter(listing_id=listing_id)
        return queryset
