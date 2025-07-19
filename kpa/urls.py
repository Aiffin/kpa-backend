from django.urls import path
from .views import WheelSpecificationAPIVIEW

urlpatterns=[
    path('forms/wheel-specifications/',WheelSpecificationAPIVIEW.as_view(),name="wheelSpeccification")
]