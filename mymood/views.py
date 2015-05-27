from django.shortcuts import render
from math import pi
from django.template import Template, Context

# Create your views here.

from django.http import HttpResponse

def welcomepage(request):
    return HttpResponse(pi)


def templateabout():
    template_about = """<!DOCTYPE html>
                        <html lang="en">
                        <head>
                          <title>Bootstrap Example</title>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1">
                          <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
                          <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
                          <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
                        </head>
                        <body>

                        <div class="container">
                          <h1>Your Mood Music</h1>
                          <p>Site under developement</p>
                          <p>Project can be found at: https://github.com/tmdavid/mymoodApp.</p>
                        </div>

                        </body>
                        </html>
                    """
    t = Template(template_about)
    return t

def about(request):
    response = templateabout()
    html = response.render(Context())
    return HttpResponse(html)
