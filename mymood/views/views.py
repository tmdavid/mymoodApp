from django.shortcuts import render
from math import pi
from django.template import Template, Context

# Create your views here.

from django.http import HttpResponse

def welcomepage(request):
    return HttpResponse(pi)



