from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Products, Categories
from django.core.paginator import Paginator

# Create your views here.

def index(request, cat_id = None):
    product_content = Products.objects.all()
    category_content = Categories.objects.all()

    cat_id = request.GET.get('category')
    sort_param = request.GET.get('sort')

    if cat_id:
        product_content = product_content.filter(category_id=cat_id)

    if sort_param == 'price_asc':
        product_content = product_content.order_by('price')
    if sort_param == 'price_desc':
        product_content = product_content.order_by('-price')
    if sort_param == 'promotion':
        product_content = product_content.filter(discount__gt=0)
    if sort_param == 'new_product':
        product_content = product_content.order_by('-created_at')

    return render(
        request,
        "product/index.html",
        {
            "products": product_content,
            "category": category_content,
            "current_sort": sort_param,
            "current_category": cat_id,
        }
    )


def about(request):
    return render(
        request,
        "product/about_us.html"
    )

def basket(request):
    return render(
        request,
        "product/basket.html"
    )