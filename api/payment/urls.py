from rest_framework import routers
from django.urls import path, include
from . import views


urlpatterns = [
    

    path('gettoken/<str:id>/<str:token>/',views.generate_token, name="token.generate"),

    path('process/<str:id>/<str:token>/',views.procress_payment, name="process.payment"),
]
