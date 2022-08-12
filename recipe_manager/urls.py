"""recipe_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.login),
    path('signup/', core_views.signup),
    path('index/', core_views.index),
    path('register/', core_views.register),
    path('search/', core_views.search),
    path('order/', core_views.order),
    path('detail/', core_views.detail),
    path('edit/', core_views.edit),
    path('add/', core_views.add),
    path('validate/',core_views.validate),
    path('add_delete/',core_views.add_delete),
    path('index/account.html', core_views.account),
    path('index/login.html', core_views.logout),
    path('index/account1.html', core_views.manage_data),
    path('change_data/', core_views.change_data),
    path('edit_2/', core_views.edit_2),
    path('detail/account.html', core_views.account),
    path('detail/account1.html', core_views.manage_data),
    path('edit_2/account.html', core_views.account),
    path('edit_2/account1.html', core_views.manage_data),
    path('edit/account.html', core_views.account),
    path('edit/account1.html', core_views.manage_data),
    path('detail/login.html', core_views.logout),
    path('edit/login.html', core_views.logout),
    path('edit_2/login.html', core_views.logout),
    path('account/login.html', core_views.logout),
    path('account1/login.html', core_views.logout)

]
