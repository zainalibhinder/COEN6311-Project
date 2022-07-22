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
sys.path.append('./core')
from list_database import lists

users = pd.read_csv("users.csv")
lists = lists()

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))

def order(request):
    template = loader.get_template('orders.html')
    return HttpResponse(template.render({}, request))

def charts(request):#添加了charts
    template = loader.get_template('charts.html')
    return HttpResponse(template.render({}, request))

def index(request):
    global lists
    lists_name = lists.get_listnames()
    list_chosen = request.GET.get('list_chosen')
    print(list_chosen)
    if list_chosen == None:
        list_transfer = lists.get_full_list()
        name_display = 'Welcome using the recipe management system!'
    else:
        list_transfer = lists.search(list_chosen, 'list_name')
        name_display = list_chosen
    print(list_transfer)
    template = loader.get_template('index.html')
    context = {
        'list_transfer' : list_transfer,
        'lists_name' : lists_name,
        'name_display' : name_display,
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
