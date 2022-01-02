from django.urls import path
from .views import DoctorList, DoctorDetail, AppointmentDetail, AppointmentList

urlpatterns = [
    path("", DoctorList.as_view(), name="Doctor_list"),
    path("<int:pk>/", DoctorDetail.as_view(), name="Doctor_detail"),
    path("appointment/", AppointmentList.as_view(), name="Appointment_list"),
    path("appointment/<int:pk>/", AppointmentDetail.as_view(), name="Appointment_detail"),
]