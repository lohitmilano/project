'''
URL Mapping with handler
'''


from django.conf.urls import patterns, include, url

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from .productapiHandler import ProductApiHandler, ProductApiCatHandler

from project.api.apihandler.productapiExtendedHandler import ProductApiExtendedHandler
from django.views.decorators.cache import cache_page

auth = HttpBasicAuthentication()
ad = {'authentication': auth}

#TODO: add this api definition to readme
add_product_handler = Resource(handler=ProductApiExtendedHandler, **ad)

#TODO: add category from API
#add_category_handler = Resource(handler=ProductApiExtendedHandler, **ad)

urlpatterns = patterns('',
    url(r'^getproduct/(?P<product_id>\d+)/$', Resource(ProductApiHandler)),
    url(r'^getproduct/(?P<product_id>\d+)/xml/$', Resource(ProductApiHandler), { 'emitter_format': 'xml' }),


    url(r'^allproduct/$', Resource(ProductApiHandler)),
    url(r'^allproduct/xml/$', Resource(ProductApiHandler),{ 'emitter_format': 'xml' }),

    url(r'^category/(?P<cat_id>\d+)/$', Resource(ProductApiCatHandler)),
    url(r'^category/(?P<cat_id>\d+)/xml/$', Resource(ProductApiCatHandler), { 'emitter_format': 'xml' }),

    #productapiExtended
    url(r'^extend/allproduct/$', Resource(ProductApiExtendedHandler)),
    #url(r'^extend/allproduct/xml/$', Resource(ProductApiExtendedHandler), { 'emitter_format': 'xml' }),

    url(r'^extend/allproduct/xml/$', cache_page(60*1)(Resource(ProductApiExtendedHandler)), { 'emitter_format': 'xml' }),

    url(r'^extend/category/(?P<cat_id>\d+)/$', Resource(ProductApiExtendedHandler)),
    url(r'^extend/category_name/(?P<cat_name>\w+)/$', Resource(ProductApiExtendedHandler)),

    # POST API
    url(r'^extend/add_product/$', add_product_handler),
   # url(r'^extend/add_category/$', Resource(add_category_handler)),
)
