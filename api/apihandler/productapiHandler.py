
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate
from django.core.exceptions import ObjectDoesNotExist

import logging
from project.api.productapi.models import Product, ProductCategory

from project.api.utility import errorCodes
from project.api.utility.apiUtility import ApiUtility, Error, Success

class ProductApiHandler(BaseHandler):
    allowed_methods = ('GET')
    model = Product
    fields=("id", "product_title","name","author", "thumb")


    @throttle(10, 1*60) # 10 call per minute
    def read(self, request, product_id=None,*args, **kwargs):
        try:
            if "allproduct" in request.path:
                return Product.objects.all()

            if "getproduct" in request.path:
                return Product.objects.get(pk=product_id)

            return Error(errorCodes.NOT_FOUND, 'request not found').__dict__()
        except ObjectDoesNotExist:
            return Error(errorCodes.BAD_REQUEST, 'bad request').__dict__()



class ProductApiCatHandler(BaseHandler):
    allowed_methods = ('GET')
    model = ProductCategory
    fields=("id","publish_data", "product_title","name","author")

    def read(self, request,*args, **kwargs):
        try:
            #user = kwargs['cat_id']
            #start = kwargs.get('start', 0)
            return Product.objects.filter(product_cat=ProductCategory.objects.get(pk=kwargs['cat_id']))
            #return {"error":"Error"}
        except ObjectDoesNotExist:
            return {"error":"not found"}