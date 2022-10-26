from django.shortcuts import render
from .models import *
# Create your views here.

def mainpage(request):

    new_left_side = news.objects.all()[:1]
    new_right_side = news.objects.all()[1:2]
    new_center_top = news.objects.all()[2:3]
    new_center_bottom = news.objects.all()[3:5]

    context = {
        'new_left_side' : new_left_side,
        'new_right_side' : new_right_side,
        'new_center_top' : new_center_top,
        'new_center_bottom' : new_center_bottom,
    }

    return render(request,"index.html", context)