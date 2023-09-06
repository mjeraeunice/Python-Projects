from rest_framework import serializers
from Customer.models import Customer
from Delivery.models import Delivery
from inventory.models import Product
from order.models import Order
from payment.models import Payment
from Reviews.models import Review

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model=Delivery
        fields ='__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields= '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        models =Payment
        fields='__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        models=Review
        fields='__all__'
        

