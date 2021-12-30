from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsAuthenticatedOrReadOnly


class DoctorList(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class DoctorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)