from django.shortcuts import render, redirect

from solemne.models import Brand, Category, Product

def home(request):

    products = Product.objects.filter(status=1)

    categories = Category.objects.filter(status=1)
    
    return render(request, 'home.html', {'products':products, 'categories':categories})


def category(request,category_id):

    products = Product.objects.filter(category__id=category_id, status=1)

    categories = Category.objects.filter(status=1)

    return render(request, 'category.html', {'products':products, 'categories':categories})


def product(request,product_id):
    products = Product.objects.filter(id=product_id, status=1)

    return render(request, 'product.html', {'products':products})