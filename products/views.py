from django.http import Http404
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404

from .models import Product


# Create your views here.
class ProductFeaturedListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/list.html"
    def get_queryset(self, *args, **kwargs):
        request=self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"
    # def get_queryset(self, *args, **kwargs):
    #     request=self.request
    #     return Product.objects.featured()

class ProductListView(ListView):
    template_name = "product/list.html"


class Product_detail_Slug_view(DetailView):
    queryset = Product.objects.all()
    template_name ="products/detail.html"




def product_list_view(request):

    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)



def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk) #id
    #instance= get_object_or_404(Product,pk=pk)
    # try:
    #     instance=Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("product doesnot exist")
    # except:
    #     print("huh?")
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesnot exist")
    # print(instance)
    # qs= Product.objects.filter(id=pk)
    #
    # #print(qs)
    # if qs.exists() and  qs.count()==1: #len(qs)
    #     instance=qs.first()
    # else:
    #     raise Http404("product does not exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
