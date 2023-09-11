from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Product


# Create your views here.
def all_products(request):
    '''A view to show products

    Args:
        request: HTTP request
    '''
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'You did not enter any search criteria!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
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
