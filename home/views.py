from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def credits(requests):
    content = 'Nivland\nVladimir'
    return HttpResponse(content, content_type = 'text/plain')
