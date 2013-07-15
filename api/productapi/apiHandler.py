'''
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate
from django.core.exceptions import ObjectDoesNotExist

import logging

from api.productapi.models import Product, ProductCategory

class ApiHandler(BaseHandler):
    allowed_methods = ('GET')
    model = ProductCategory

    def read(self, request, cat_id):
        try:
            logging.error("=======GET===============")
            return self.model.objects.get(pk = cat_id)
        except ObjectDoesNotExist:
            return {"error":"not found"}



'''