from django.shortcuts import render
from .models import ProductCategory, Product

title = 'Главная'
links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
]

same_products ='same__products'


def main(request):
    title = 'Главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html')


def products(request):
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    return render(request, 'mainapp/contact.html')

