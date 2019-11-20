from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Category

# Create your views here.
def home(request):
    categorys = Category.objects.all()
    return render(request, 'home.html', {'categorys':categorys})