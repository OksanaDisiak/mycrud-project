#from rest_framework import viewsets
from django.shortcuts import render
from .serializers import DriverSerializer
from .models import Driver
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# class DriverViewSet(viewsets.ModelViewSet):
#     queryset = Driver.objects.all().order_by('id')
#     serializer_class = DriverSerializer

class DriverView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response({'drivers': serializer.data})

    def get(self, request, pk):
        driver = get_object_or_404(Driver.objects.all(), pk=pk)
        serializer = DriverSerializer(data=driver)
        return Response({'driver': serializer.data})


    def post(self, request):
        driver = request.data.get('driver')

        serializer = DriverSerializer(data=driver)
        if serializer.is_valid(raise_exception=True):
            driver_saved = serializer.save()
        return Response({"success": "Driver '{}' created successfully".format(driver_saved.id)})

    def put(self, request, pk):
        saved_driver = get_object_or_404(Driver.objects.all(), pk=pk)
        data = request.data.get('driver')
        serializer = DriverSerializer(instance=saved_driver, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            driver_saved = serializer.save()
        return Response({
            "success": "Driver '{}' updated successfully".format(driver_saved.id)
        })

    def delete(self, request, pk):
        driver = get_object_or_404(Driver.objects.all(), pk=pk)
        driver.delete()
        return Response({
            "message": "Driver with id `{}` has been deleted.".format(pk)
        })



