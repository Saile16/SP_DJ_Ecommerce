# por ahora y para ejemplos usaremos otro import
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .forms import ProductModelForm
from .models import Product
# Create your views here.


def search_view(request, *args, **kwargs):
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    context = {"name": "Justin", "query": query}
    print(query, qs)
    return render(request, 'home.html', context)


# def product_create_view(request, *args, **kwargs):
#     print(request.POST)
#     print(request.GET)
#     if request.method == 'POST':
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 # de esta menra obtenemos lo que ingreso el usuario
#                 print(my_form.cleaned_data.get("title"))
#                 title_from_input = my_form.cleaned_data.get("title")
#                 Product.objects.create(title=title_from_input)
#                 # print("post_data", post_data)
#     return render(request, 'forms.html', {})

def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do some stuff y guardarlo
        obj.save()
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # Product.objects.create(**data)
        form = ProductModelForm()
    return render(request, 'forms.html', {"form": form})


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


# def bad_view(request, *args, **kwags):
#     print(dict(request.GET))
#     my_request_data = dict(request.GET)
#     new_product[0] = my_request_data.get("new_product")
#     if new_product.lower() == "true":
#         print("new Product")
#         Product.objects.create(title=my_request_data.get(
#             'title')[0], content=my_request_data.get('content')[0])
#     return HttpResponse("Dont do this")
