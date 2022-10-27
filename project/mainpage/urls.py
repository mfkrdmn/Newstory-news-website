from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('singlepage/<str:pk>', views.singlePage, name="singlePage"),
]
