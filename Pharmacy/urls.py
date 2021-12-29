from django.urls import path
from .views import ParmacyList, PharmacyDetail

urlpatterns = [
    path("", ParmacyList.as_view(), name="pharmacy_list"),
    path("<int:pk>/", PharmacyDetail.as_view(), name="pharmacy_detail"),
]