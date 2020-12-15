from django.shortcuts import render
from .models import ProductCategory, Product

title = 'Главная'


def main(request):

    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    print(pk)

    products = Product.objects.all()
    category = Product.objects.filter(category=pk)


    content = {'title': title, 'products': products, 'category': category}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')






