from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    id = models.CharField(max_length=15, unique=True, primary_key=True)
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField()
    
    date_joined = models.DateTimeField(
        verbose_name="date joined",
        auto_now_add=True
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id', 'email', ]

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    present_item = models.IntegerField(default=0)
    ordered_times=models.IntegerField(default=0)

    def __str__(self):
        return self.name


def customer_photo_directory(instance, filename):
    return 'customers/{0}_{1}'.format(instance.identity, instance.name)


class Customer(models.Model):
    identity = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=9999)
    

    def __str__(self):
        return '{0} ({1})'.format(self.identity, self.name)


class Order(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.name

class OrderItem(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    
    
   
    
    