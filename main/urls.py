from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('beta-download', views.beta),
    path('getCode', views.getCode),
    path("<str:path>", views.route_all)
]
