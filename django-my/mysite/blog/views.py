from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello World!')

# def bad_request(request):
#     return render(request, 400.html)
#
# def permission_denied(request):
#     return render(request, 403.html)
#
# def page_not_found(request):
#     return render(request, 404.html)
#
# def page_error(request):
#     return render(request, 500.html)
