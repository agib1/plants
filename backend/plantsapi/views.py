from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Plant, Request
from .serializers import PlantsSerializer, RequestSerializer
from rest_framework.decorators import api_view
from rest_framework import status
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


class RequestsView(generics.RetrieveAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RequestSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
