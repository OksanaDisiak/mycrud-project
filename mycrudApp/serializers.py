from rest_framework import serializers
from .models import Driver, Vehicle

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'first_name', 'second_name')

