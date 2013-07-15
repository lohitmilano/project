from django.db import models
import os

class ProductCategory(models.Model):
    text = models.CharField(max_length=75)
    def __unicode__(self):
        return self.text

def get_image_path(instance, filename):
    return os.path.join('img', filename)

class Product(models.Model):
    
    name = models.CharField(max_length=75)
    product_title=models.CharField(max_length=100, default="product title")
    author=models.CharField(max_length=100, default="author name not set")
    product_cat = models.ForeignKey(ProductCategory, related_name="puzzle_questions")
    thumb = models.ImageField(upload_to=get_image_path)

    
    def __unicode__(self):
        return self.name


