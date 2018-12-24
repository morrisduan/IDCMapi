from django.shortcuts import render
from rest_framework import viewsets
from .models import Host
from .serializers import HostSerializer

# Create your views here.
class HostViewset(viewsets.ModelViewSet):
    queryset = Host.objects.all()[:10]
    serializer_class = HostSerializer