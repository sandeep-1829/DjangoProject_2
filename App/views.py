from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def fasak(request):
    return HttpResponse('<h1><marquee> Question : Hii Hello My Dear Friend</h1></marquee>')



def jigelrani(request):
    return HttpResponse('<h1><marquee>Reply : Hello I am Fine My Dear Friend</h1></marquee>')

