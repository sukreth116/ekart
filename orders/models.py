from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.

class Order(models.Model):

    # for trash concept delete choices
    STATUS_ACTIVE = 1
    STATUS_DELETED = 0
    DELETE_CHOICES = ((STATUS_ACTIVE, 'Live'), (STATUS_DELETED, 'Deleted'))
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default = STATUS_ACTIVE)

    # cart stage
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = ((ORDER_PROCESSED,'Order Processed'),(ORDER_DELIVERED, 'Order Delivered'), (ORDER_REJECTED, 'Order Rejected'))
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)

    customer_owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True, related_name='orders')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name = 'added_item', on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 1)
    order_owner = models.ForeignKey(Order, related_name = 'ordered_items', on_delete=models.CASCADE)
