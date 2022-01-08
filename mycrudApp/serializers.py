from rest_framework import serializers
from .models import Driver, Vehicle

# class DriverSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Driver
#         fields = ('id', 'first_name', 'second_name')

class DriverSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=250)
    second_name = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Driver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)

        instance.save()
        return instance



