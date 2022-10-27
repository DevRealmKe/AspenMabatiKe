from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.


def HomePage(request):
    products = Product.objects.all()[:3]
    galleryImages = Gallery.objects.all()

    page = request.GET.get("page", 1)
    paginator = Paginator(galleryImages, 6)

    try:
        gallery_list = paginator.page(page)
    except PageNotAnInteger:
        gallery_list = paginator.page(1)
    except EmptyPage:
        gallery_list = paginator.page(paginator.num_pages)

    return render(
        request,
        "Homeapp/Home.html",
        {
            "products": products,
            "galleryImages": galleryImages,
            "gallery_list": gallery_list,
        },
    )


def ProductsPage(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(product_category=categories)
        product_count = products.count()
    else:
        products = Product.objects.all()
        product_count = products.count()

    # productsPaging = Product.objects.all()
    # categories = Category.objects.all()

    # page = request.GET.get('page',1)
    # paginator = Paginator(productsPaging,1)

    # try:
    #     products_list = paginator.page(page)
    # except PageNotAnInteger:
    #     products_list = paginator.page(1)
    # except EmptyPage:
    #     products_list= paginator.page(paginator.num_pages)

    return render(
        request,
        "Homeapp/Products.html",
        {
            "products": products,
            "categories": categories,
            "product_count": product_count,
            # 'products_list':products_list
        },
    )


def ProductDetails(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {"product": product}
    return render(request, "Homeapp/ProductDetails.html", context)


def ContactUs(request):

    return render(request, "Homeapp/ContactUs.html")

def AboutUs(request):

    return render(request, "Homeapp/AboutUs.html")