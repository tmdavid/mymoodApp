__author__ = 'dtorrejon'
from django.shortcuts import render
from math import pi
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template

def about(request):
    #html = response.render(Context()) #inside the context place a dictionary and in the html {{ var_name }}
    t = get_template('about.html')
    html = t.render(Context())
    return HttpResponse(html)