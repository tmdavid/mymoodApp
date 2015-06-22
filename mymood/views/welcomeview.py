from django.shortcuts import render
from math import pi
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
import json
# Create your views here.

from django.http import HttpResponse
many_viewers = 0

def welcomepage(request):
    if 'focusedInput' in request.POST:
        print request.POST['focusedInput']
        print len(request.POST['focusedInput'])


    many_viewers =+1
    t = get_template('welcome.html')
    request_context = RequestContext(request)
    request_context.push({"viewer": many_viewers, "nextviewer": many_viewers+1})
    #html = t.render(Context({"viewer": many_viewers, "nextviewer": many_viewers+1}))
    html = t.render(request_context)
    return HttpResponse(html)

def create_post(request):

    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}
        print 'create_post'

        #post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = 1
        response_data['text'] = post_text
        response_data['created'] = 'now'
        response_data['author'] = 'david'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

