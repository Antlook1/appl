from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *



def index(request):
    product = Product.objects.all()
    categorys = Category.objects.all()
    context = {
        'product': product,
        'categorys': categorys,
        'title': 'Главная страница'
    }
    return render(request, 'shop/index.html', context=context)

def show_category(request, cat_id):
    product = Product.objects.filter(category_id=cat_id)
    if len(product) == 0:
        raise Http404()
    categorys = Category.objects.all()

    context = {
        'product': product,
        'categorys': categorys,
        'title': 'Категория'
    }
    return render(request, 'shop/shop.html', context=context)


def show_all(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
        'title': 'Все категории'
    }
    return render(request, 'shop/show_all.html', context=context)


def show_product(request, art):
    product = get_object_or_404(Product, id=art)
    context = {
        'product': product,
        'title': product.name,
    }
    return render(request, 'shop/shop-single.html', context=context)


def search(request):
    search_query = request.GET.get('search')
    if search_query:
        product = Product.objects.filter(name__iregex=search_query)
    else:
        product = Product.objects.all()

    return render(request, 'shop/all_prod.html', {'product': product})


def order(request, art):
    product = get_object_or_404(Product, id=art)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=art)
            form.instance.product = product
            form.save()
            return redirect('index')
    else:
        form = CreateOrderForm()
    context = {
        'form': form,
        'product': product,
        'title': 'Оформление заказа',
    }
    return render(request, 'shop/order.html', context=context)



