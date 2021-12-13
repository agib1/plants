from django.urls import path
from .views import PlantsView, PlantDetail
from django.conf.urls import url
from plantsapi import views

urlpatterns = [
    path('plants/', PlantsView.as_view()),
    path('plants/<slug:slug>/', PlantDetail.as_view())
]