
from django.conf.urls import url

from products.views import product_list_view
from products.views import Product_detail_Slug_view


urlpatterns = [

    url(r'^$', product_list_view),
    #url(r'^products/(?P<pk>\d+)/$', product_detail_view),
    url(r'^(?P<slug>[\w-]+)/$', Product_detail_Slug_view.as_view())


]
