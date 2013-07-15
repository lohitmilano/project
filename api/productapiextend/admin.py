from django.contrib import admin

from project.api.productapiextend.models import Product, ProductCategory

from django import forms
from django.forms.util import ErrorList

import logging

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

    def clean(self):
        try:
            product_name = self.cleaned_data['name']
            # form validation, error list required
            if len(product_name)<5:
                self._errors['name']=ErrorList(["Product name should have at least 5 characters"])
        except:
            pass
        return self.cleaned_data


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    search_fields = ['name']


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)

