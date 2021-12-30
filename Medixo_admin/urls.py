from django.urls import path
from .views import PharmacyDetail,ParmacyList

urlpatterns = [
    path("", ParmacyList.as_view(), name="Pharmacy_list"),
    path("<int:pk>/", PharmacyDetail.as_view(), name="Pharmacy_detail"),
]