from django.urls import path
from .views import DoctorList, DoctorDetail

urlpatterns = [
<<<<<<< HEAD
    path("", DoctorList.as_view(), name="doctor_list"),
    path("<int:pk>/", DoctorDetail.as_view(), name="doctor_detail"),
=======
    path("", DoctorList.as_view(), name="Doctor_list"),
    path("<int:pk>/", DoctorDetail.as_view(), name="Doctor_detail"),
>>>>>>> 7ba62cfdc11daecef80eb3625d30697bed52bfce
]