from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DriverSerializer
from .models import Driver

# Create your views here.

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by('id')
    serializer_class = DriverSerializer
