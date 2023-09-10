from django.shortcuts import render


# Create your views here.
def index(request):
    '''
    Render the home page

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response representing the home page.
    '''
    return render(request, 'home/index.html')
