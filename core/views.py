from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http.response import StreamingHttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
import json
import os
import sys
import time
import pandas as pd
import sys

users = pd.read_csv("users.csv")
lists = pd.read_csv("lists.csv")

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))

def index(request):
    global lists
    list_content = json.dumps(lists.values.tolist())
    print(list_content)
    template = loader.get_template('index.html')
    context = {
        'list_content' : list_content
    }
    return HttpResponse(template.render(context, request))

def register(request):
    name = request.POST.get('signup-name')
    robot_id = request.POST.get('robotID')
    email = request.POST.get('signup-email')
    password = request.POST.get('signup-password')
    record = {'name':name, 'email':email, 'password':password, 'robot_id':robot_id}
    print(record)
    global users
    users = users.append(record, ignore_index=True)
    users.to_csv("users.csv")
    return HttpResponseRedirect("/index/")

def search(request):
    content = request.POST.get('searchcontent')
    option = request.POST.get('option')
    print(content, option)
    return HttpResponseRedirect("/index/")

#def get_list(request):
    
#    return JsonResponse(list_content, safe=False)