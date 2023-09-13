from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .paginations import StandardResultsSetPagination, TravelLimitOffsetPagination
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly, IsrMineOrReadOnly
from .models import HousingReview, HousingReservation, Housing, Room, HousingAvailability, \
    HousingImage
from .serializers import HousingReviewSerializer, HousingReservationSerializer, RoomGetSerializer, \
    RoomPostSerializer, HousingGetSerializer, HousingPostSerializer, \
    HousingAvailabilityPostSerializer, HousingImageSerializer, HousingAvailabilityGetSerializer
from .filters import HousingFilter
from .utils import retrieve_currency, CurrencyParaMixin, perform_create, annotate_housing_queryset, retrieve_housetrans, \
    retrieve_room, LanguageParamMixin, retrieve_currency_for_housing


class HousingViewSet(viewsets.ModelViewSet, LanguageParamMixin, CurrencyParaMixin):
    queryset = Housing.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HousingFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = TravelLimitOffsetPagination
    ordering_fields = ['stars', 'rooms__price_per_night', 'average_rating', 'review_count']
    serializer_class = HousingPostSerializer

    def retrieve(self, request, *args, **kwargs):
        return retrieve_currency_for_housing(self, request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingGetSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = super().get_queryset()
        annotated_queryset = annotate_housing_queryset(queryset)
        return annotated_queryset

    def housetrans(self, serializer, *args, **kwargs):
        return retrieve_housetrans(self, serializer)


class HousingReservationViewSet(viewsets.ModelViewSet):
    queryset = HousingReservation.objects.all()
    serializer_class = HousingReservationSerializer
    permission_classes = [IsrMineOrReadOnly]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)
        return perform_create(self, serializer)

    def get_queryset(self):
        return HousingReservation.objects.filter(user=self.request.user)


class HousingAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = HousingAvailability.objects.all()
    serializer_class = HousingAvailabilityPostSerializer
    permission_classes = [IsOwnerUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingAvailabilityGetSerializer
        return self.serializer_class


class RoomViewSet(viewsets.ModelViewSet, CurrencyParaMixin, LanguageParamMixin):
    queryset = Room.objects.all()
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = StandardResultsSetPagination
    serializer_class = RoomPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        return retrieve_currency(self, request, *args, **kwargs)

    def room_translate(self, serializer, *args, **kwargs):
        return retrieve_room(self, serializer)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsClientUserOrReadOnly]


class HousingImageSet(viewsets.ModelViewSet):
    queryset = HousingImage.objects.all()
    serializer_class = HousingImageSerializer
    permission_classes = [IsOwnerUserOrReadOnly]
