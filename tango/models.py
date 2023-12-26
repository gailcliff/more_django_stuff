from django.db import models

# Create your models here.


class Customer(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('na', 'Prefer not to say')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDERS)

    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ProductTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    tag = models.ManyToManyField(to=ProductTag)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.description}"


class Order(models.Model):
    STATUS = (('pending', 'Pending'), ('ofd', 'Out for delivery'), ('delivered', 'Delivered'))

    customer = models.ForeignKey(to=Customer, on_delete=models.RESTRICT, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.RESTRICT, null=True)
    status = models.CharField(max_length=100, choices=STATUS)
    date_made = models.DateTimeField(auto_now_add=True)
