from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Plant
from .serializers import PlantsSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.

class PlantsView(generics.RetrieveAPIView):
    queryset = Plant.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PlantsSerializer(queryset, many=True)

        return Response(serializer.data)

class PlantDetail(generics.RetrieveAPIView):
    
    def get(self, request, slug):
        queryset = Plant.objects.get(slug=slug)
        serializer = PlantsSerializer(queryset)

        return Response(serializer.data)