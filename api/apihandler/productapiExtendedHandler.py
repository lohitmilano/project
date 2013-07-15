from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate

from project.api.utility import errorCodes

from project.api.productapiextend.models import Product, ProductCategory
from project.api.utility.apiUtility import ApiUtility, Error, Success

import logging
import sys

class ProductApiExtendedHandler(BaseHandler):
    allowed_methods = ('GET','POST')
    model = Product
    fields=("id","publish_data", "product_title","name","author","product_cat")


    def read(self, request,*args, **kwargs):
        try:
            logging.error(request.path)

            if ApiUtility.get_function_name(request.path)=='allproduct':
                return Product.objects.all()

            if ApiUtility.get_function_name(request.path)=='category':
                #return Product.objects.filter(product_cat__text = 'child').values("name","id","product_title")
                return Product.objects.filter(product_cat__pk = kwargs['cat_id']).values("name","id","product_title")

            if ApiUtility.get_function_name(request.path)=='category_name':
                return Product.objects.filter(product_cat__text = kwargs['cat_name'] ).values("name","id","product_title")
                #return Product.objects.filter(product_cat__pk = kwargs['cat_id']).values("name","id","product_title")

            return Error(errorCodes.NOT_FOUND, 'request not found').__dict__()
        except :
            return Error(errorCodes.BAD_REQUEST, 'bad request').__dict__()
            #return Success(True).__dict__()

    #@classmethod
    #def product_cat(self, model):
    #    return model.product_cat.values("text","id")

    def create(self, request):

        try:
            if not attrs.has_key('product_name') or  not attrs.has_key('category_id'):
                return Error(error_codes.BAD_REQUEST, 'Missing parameters').__dict__()

            attrs = self.flatten_dict(request.POST)
            if ApiUtility.get_function_name(request.path)=='add_product':
                product_name =attrs.get('product_name',None)
                cat_id =attrs.get('category_id',None)

                if product_name==None or cat_id==None:
                    return Error(error_codes.BAD_REQUEST, 'Invalid parameters').__dict__()


                product = Product.objects.create(name=product_name) # TODO: should use get or create
                product.save()
                product.product_cat.add(cat_id) #m2m field

            return product
        except:
            return Error(errorCodes.BAD_REQUEST, 'bad request').__dict__()