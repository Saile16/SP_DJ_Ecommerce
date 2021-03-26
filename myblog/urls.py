"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views
# una manera mas limpia o correcta de importan esto seria
from products.views import (
    home_view,
    product_detail_view,
    product_api_detail_view,
    product_list_view

)

urlpatterns = [
    path('search/', home_view),
    path('products/', product_list_view),
    path('products/<int:pk>/', product_detail_view),
    path('api/products/<int:pk>/', product_api_detail_view),
    path('products/1/', product_detail_view),
    path('admin/', admin.site.urls),
]
