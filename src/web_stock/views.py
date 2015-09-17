from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
# Create your views here.

def test(request):
    return render_to_response('test.html',RequestContext(request))