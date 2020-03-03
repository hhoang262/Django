from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("Response from Categories")
    return render(request, 'categories/index.html')
