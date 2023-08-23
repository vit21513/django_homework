from django.db import models


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    data_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} email {self.email} phone number {self.phone_number}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantu = models.IntegerField()
    data_adding = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Product name {self.name} price {self.price} usd, quanty {self.quantu} description {self.description}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.FloatField(default=0)
    data_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order client {self.client} product {self.product} total cost {self.total_price}'
