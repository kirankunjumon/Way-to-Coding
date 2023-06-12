
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect


# Basic View
def hello(request):
    return HttpResponse("Hello, world!")
  
# Dynamic View
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")

# Template View
def home(request):
    return render(request, 'home.html')

# Dynamic Template View
def post_detail(request, post_id):
    context = {
        "data": 123
    }
    return render(request, 'post_detail.html', context)

# JSON View
def api_data(request):
    data = {'key': 'value', 'key2': 'value2'}
    return JsonResponse(data)

# Redirect View
def redirect_to_home(request):
    return redirect('home')