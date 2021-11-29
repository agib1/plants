from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Test
from .serializers import TestSerializer

# Create your views here.

class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TestSerializer(queryset, many=True)

        return Response(serializer.data)

