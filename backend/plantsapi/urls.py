from django.urls import path
from .views import PlantsView, PlantDetail, RequestsView


urlpatterns = [
    path('plants/', PlantsView.as_view(), name="list"),
    path('plants/<slug:slug>/', PlantDetail.as_view(), name="single"),
    path('requests/', RequestsView.as_view(), name="req")
]