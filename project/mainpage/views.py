from django.shortcuts import render
from .models import *
# Create your views here.

def mainpage(request):

    new = news.objects.all()

    context = {
        'new' : new
    }

    return render(request,"index.html", context)