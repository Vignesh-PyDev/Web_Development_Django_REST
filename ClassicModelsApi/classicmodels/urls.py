from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Customer_List, name = "Customer_List"),
    path('detail/<str:pk>/', views.Customer_Detail, name = "Customer_Detail"),
    path('addNew', views.Customers_Create, name = "Customers_Create"),
    path('UpdateOne/<str:pk>/', views.Customers_Update, name = "Customers_Update"),
]