from django.shortcuts import render
from rest_framework.views import APIView
from Customer.models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from Delivery.models import Delivery
from.serializers import DeliverySerializer
from Reviews.models import Review
from.serializers import ReviewSerializer
from.serializers import OrderSerializer
from order.models import Order
from.serializers import PaymentSerializer
from payment.models import Payment
from inventory.models import Product
from.serializers import InventorySerializer

# Create your views here.
class CustomerListView(APIView):
    def get(self,request):
       customers=Customer.objects.all() ###querried data
       serializer=CustomerSerializer(customers,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    def get(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         customer=Customer.objects.get(id=id)
         customer.delete()

         return Response("customer deleted successfully",status=status.HTTP_204_NO_CONTENT)

class DeliveryListView(APIView):
    def get(self,request):
       deliveries=Delivery.objects.all() ###querried data
       serializer=DeliverySerializer(deliveries,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=DeliverySerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
class DeliveryDetailView(APIView):
    def get(self,request,id,format=None):
        delivery=Delivery.objects.get(id=id)
        serializer=DeliverySerializer(delivery)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        delivery=Delivery.objects.get(id=id)
        serializer=DeliverySerializer(delivery,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         delivery=Delivery.objects.get(id=id)
         delivery.delete()

         return Response("delivery details deleted successfully",status=status.HTTP_204_NO_CONTENT)
    
class ReviewsListView(APIView):
    def get(self,request):
       reviews=ReviewSerializer.objects.all() ###querried data
       serializer=CustomerSerializer(reviews,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class ReviewDetailView(APIView):
    def get(self,request,id,format=None):
        review=Review.objects.get(id=id)
        serializer=ReviewSerializer(review)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        review= Review.objects.get(id=id)
        serializer=ReviewSerializer(review,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         review=Review.objects.get(id=id)
         review.delete()

         return Response("review deleted successfully",status=status.HTTP_204_NO_CONTENT)
    
class OrderListView(APIView):
    def get(self,request):
       orders=OrderSerializer.objects.all() ###querried data
       serializer=OrderSerializer(orders,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class OrderDetailView(APIView):
    def get(self,request,id,format=None):
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        order= Order.objects.get(id=id)
        serializer=OrderSerializer(order,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         order=Order.objects.get(id=id)
         order.delete()

         return Response("order deleted successfully",status=status.HTTP_204_NO_CONTENT)
    
class PaymentListView(APIView):
    def get(self,request):
       payments=Payment.objects.all() ###querried data
       serializer=PaymentSerializer(payments,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=PaymentSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class PaymentDetailView(APIView):
    def get(self,request,id,format=None):
        payment=Payment.objects.get(id=id)
        serializer=OrderSerializer(payment)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        payment= Payment.objects.get(id=id)
        serializer=OrderSerializer(payment,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         payment=Payment.objects.get(id=id)
         payment.delete()

         return Response("order deleted successfully",status=status.HTTP_204_NO_CONTENT)  

class InventoryListView(APIView):
    def get(self,request):
       payments=Payment.objects.all() ###querried data
       serializer=PaymentSerializer(payments,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=PaymentSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class InventoryDetailView(APIView):
    def get(self,request,id,format=None):
        payment=Payment.objects.get(id=id)
        serializer=OrderSerializer(payment)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        payment= Payment.objects.get(id=id)
        serializer=OrderSerializer(payment,request.data)
            
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
         payment=Payment.objects.get(id=id)
         payment.delete()

         return Response("order deleted successfully",status=status.HTTP_204_NO_CONTENT)  

