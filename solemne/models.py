from __future__ import unicode_literals
from sorl.thumbnail import ImageField
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/brand',blank=True, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    banner = models.ImageField(upload_to='images/banner_categories',blank=True,null=True)
    sort_order = models.IntegerField(default=0)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, null=True)
    category = models.ForeignKey(Category, null=True)
    status = models.BooleanField()
    image = models.ImageField(upload_to='images/data',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku