from enum import unique
from re import T
from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.
class HomeDetail(models.Model):
    name  = models.CharField(max_length=250, )
    headline = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='images/logo')
    
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200,unique=True)
    product_desc = models.TextField()
    createdat = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to="images/products",blank=True,null=True)

    def __str__(self):
        return self.product_name

class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to="images/gallery", null=True,blank=True)

    # def __str__(self):
    #     return self.gallery_image
