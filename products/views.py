# por ahora y para ejemplos usaremos otro import
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Product
# Create your views here.


def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    context = {"name": "Justin"}
    return render(request, 'home.html', context)


def product_detail_view(request, pk):
    # obj = Product.objects.get(id=id)
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    # try:
    #     obj=Product.objects.get(id=id)
    # except:
    #     raise Http404
    # return HttpResponse(f"Product id {obj.id} ")
    return render(request, 'products/detail.html', {'object': obj})


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "not Found"})
    return JsonResponse({"id": obj.id})
# class HomeView():
# pass


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)
