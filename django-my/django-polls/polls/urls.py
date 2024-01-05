'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: urls.py
@time: 23/9/1 10:16
@desc: 
'''

from django.urls import path
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("results/<int:pk>/", views.ResultsView.as_view(), name="results"),       # 根据路由目录进行，参数位置也是按照位置
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),       # 根据路由目录进行，参数位置也是按照位置
    path("vote/<int:question_id>/", views.vote, name="vote"),
]
