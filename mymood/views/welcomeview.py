from django.shortcuts import render
from math import pi
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

from django.http import HttpResponse

def welcomepage(request):
    t = get_template('welcome.html')
    html = t.render(Context())
    return HttpResponse(html)



