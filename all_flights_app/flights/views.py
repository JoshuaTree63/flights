from django.http import JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet

from all_flights_app.flights import serializers
from all_flights_app import models
from all_flights_app.flights.filters import FlightsFilterSet
from all_flights_app.flights.permissions import FlightsPermissions
from all_flights_app.models import Flight


class FlightsViewSet(ModelViewSet):

    serializer_class = serializers.FlightSerializer
    queryset = models.Flight.objects.all()
    filterset_class = FlightsFilterSet
    permission_classes = (FlightsPermissions, )

    @action(['GET'], detail=False)
    def stats(self):
        self.get_queryset()


@api_view(['GET'])
def get_origin_cities(request):
    all_origins = list(Flight.objects.order_by().value_list('origin_city').distinct())
    all_origins = [city for sublist in all_origins for city in sublist]

    print(all_origins)
    return JsonResponse(data=list(all_origins), safe=False)






