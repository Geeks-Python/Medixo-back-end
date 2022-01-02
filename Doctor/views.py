from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import DoctorSerializer, AppointmentSerializer
from .models import Doctor, Appointment
from .permissions import IsAuthenticatedOrReadOnly


class DoctorList(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly
    serializer_class = DoctorSerializer


class AppointmentList(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly
    serializer_class = AppointmentSerializer