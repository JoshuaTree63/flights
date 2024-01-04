from rest_framework.serializers import ModelSerializer
from all_flights_app.models import BoardingPass

class BoardingPassSerializer(ModelSerializer):

    class Meta:
        model = BoardingPass
        fields = '__all__'


