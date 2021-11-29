from django.urls import path
from .views import TestView

urlpatterns = [
    path('api/tests/', TestView.as_view(), name='tests_view')
]