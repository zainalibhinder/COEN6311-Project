from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http.response import StreamingHttpResponse
from django.template import RequestContext, loader
import os
import sys
import time

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))
