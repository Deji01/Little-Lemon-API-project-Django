from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Cart, Order, OrderItem
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    signup_date = serializers.DateTimeField(
        write_only=True, default=datetime.now)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'signup_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category']


class CartSerializer(serializers.ModelSerializer):
    menuitem_title = serializers.CharField(
        source='menuitem.title', read_only=True)
    menuitem_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='menuitem.price', read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'menuitem', 'menuitem_title',
                  'menuitem_price', 'quantity', 'unit_price', 'price']
        extra_kwargs = {
            'price': {'read_only': True},
        }


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(
        write_only=True, default=datetime.now)
    orders_items = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status',
                  'total', 'order_date', 'order_items']
        extra_kwargs = {
            'total': {'read_only': True}
        }

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(order_items, many=True, context={
                                         'request': self.context['request']})
        return serializer.data


class OrderItemSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='menuitem.price', read_only=True)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, read_only=True)
    menuitem_title = serializers.CharField(source='menuitem.title')

    class Meta:
        model = OrderItem
        fields = ['menuitem_title', 'unit_price', 'quantity', 'price']
        extra_kwargs = {
            'menuitem_title': {'read_only': True}
        }
