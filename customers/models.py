from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    STATUS_ACTIVE = 1
    STATUS_DELETED = 0
    DELETE_CHOICES = ((STATUS_ACTIVE, 'Active'), (STATUS_DELETED, 'Deleted'))
    name = models.CharField(max_length = 20)
    address = models.TextField()
    phone = models.IntegerField()
    user = models.OneToOneField(User,related_name = 'customer_profile', on_delete = models.CASCADE)
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default = STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
