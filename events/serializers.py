from rest_framework import serializers
from .models import Eventer

# Create your views here.
class EventerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventer
        fields = '__all__'

