from rest_framework import serializers
from classicmodels.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offices
        fields = "__all__"



class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"                        



class ProductlinesPaymentsProductlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productlines
        fields = "__all__" 




class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"              


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"       