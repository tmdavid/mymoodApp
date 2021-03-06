import json


from django.template import RequestContext
from django.template.loader import get_template

from mymood import config
from mymood import const

# Create your views here.

from django.http import HttpResponse

const.max_last_viewers = 5

def append_last_viewers(data):
    print 'append_last_viewers'
    config.last_viewers.append(data)
    for viewer in config.last_viewers:
        print viewer
    return True

def welcomepage(request):

    if 'focusedInput' in request.POST:
        print request.POST['focusedInput']
        print len(request.POST['focusedInput'])

    config.many_viewers += 1
    t = get_template('welcome.html')
    request_context = RequestContext(request)
    request_context.push({"viewer": config.many_viewers, "nextviewer": config.many_viewers+1})
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

        print append_last_viewers(response_data)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

