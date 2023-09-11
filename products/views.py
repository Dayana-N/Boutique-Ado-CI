from django.shortcuts import get_object_or_404, render

from .models import Product


# Create your views here.
def all_products(request):
    '''A view to show products

    Args:
        request: HTTP request
    '''
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    '''A view to render single product page

    Args:
        request: HTTP request
        product_id: Product pk

    Returns:
        Single product page, context with the product object
    '''
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
