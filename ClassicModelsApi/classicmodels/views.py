from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def Customer_List(request):
	Customer_Data = Customers.objects.all()
	serializer = CustomerSerializer(Customer_Data,many = True)
	return Response(serializer.data)


@api_view(['GET'])
def Customer_Detail(request,pk):
	try:
		Customer_Data = Customers.objects.get(customernumber = pk)
		serializer = CustomerSerializer(Customer_Data,many = False)
		if serializer.data:
			return Response(serializer.data)
	except Customers.DoesNotExist:
		return Response("Customer Detail Not Found")

@api_view(['POST'])
def Customers_Create(request):
	print("Inside Pay create",request.data)
	serializer = CustomerSerializer(data = request.data)

	if serializer.is_valid():

		# print(serializer.data,"sdfsj")
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def Customers_Update(request,pk):
	try:
		Customer_Data = Customers.objects.get(customernumber = pk)
		serializer = CustomerSerializer(instance = Customer_Data,data = request.data)
		
		if serializer.is_valid():
			print(serializer.validated_data)
			serializer.save()
			return Response(serializer.data)
	except Customers.DoesNotExist:
		return Response("Customers Detail Not Found")



@api_view(['DELETE'])
def Customers_Delete(request,pk):
	print("delete")
	try:
		Customer_Data = Customers.objects.get(customernumber = pk)
		Customer_Data.delete()
		return Response("Data Deleted")
	except Customers.DoesNotExist:
		return Response("Customers Detail Not Found")


