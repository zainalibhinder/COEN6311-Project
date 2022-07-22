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
from user_database import users

users = users()
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

def detail(request):
    recipe_name = str(request.GET.get('name'))
    global lists
    details = lists.get_recipe_detail(recipe_name)
    print(details[2])
    context = {
        'recipe_name' : recipe_name,
        'list_name' : details[0],
        'recipe_description' : details[1],
        'photo_path' : details[2],
    }
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(context, request))

def index(request):
    global lists
    lists_name = lists.get_listnames()
    list_chosen = request.GET.get('list_chosen')
    if list_chosen == None:
        list_transfer = lists.get_full_list()
        name_display = 'Welcome using the recipe management system!'
    else:
        list_transfer = lists.search(list_chosen, 'list_name')
        name_display = list_chosen
    template = loader.get_template('index.html')
    context = {
        'list_transfer' : list_transfer,
        'lists_name' : lists_name,
        'name_display' : name_display,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    name = str(request.POST.get('signup-name'))
    robot_id = str(request.POST.get('robotID'))
    email = str(request.POST.get('signup-email'))
    password = str(request.POST.get('signup-password'))
    record = {'name':name, 'email':email, 'password':password, 'robot_id':robot_id}
    global users
    users.append(record)
    return HttpResponseRedirect("/index/")

def search(request):
    content = request.POST.get('searchcontent')
    option = request.POST.get('option')
    print(content, option)
    return HttpResponseRedirect("/index/")

def validate(request):
    global users
    email = request.POST.get('signin-email')
    password = request.POST.get('signin-password')
    if users.login(email, password):
        return HttpResponseRedirect("/index/")
