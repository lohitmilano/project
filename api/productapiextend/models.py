from django.db import models

import logging

class ProductCategory(models.Model):
    text = models.TextField(max_length=1024)
    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    '''
    Many to many field example
    '''
class Product(models.Model):
    name = models.CharField(max_length=75)
    product_title=models.CharField(max_length=100, default="product title")
    author=models.CharField(max_length=100, default="author name not set")
    publish_data=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    product_cat = models.ManyToManyField(ProductCategory, related_name="product_category", null=True)

    def __unicode__(self):
        return self.name

    #TODO: when add a product to category update total product no under a category

    def save(self, *args, **kwargs):
        try:
            self.name=self.name.lower()
            super(Product, self).save(*args, **kwargs)
        except :
            pass


    @staticmethod
    def is_product_exists(product_id):
        try:
            Product.objects.get(pk=product_id)
            return True
        except :
            return False;


