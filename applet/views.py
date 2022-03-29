from django.http import HttpResponse
from django.shortcuts import render

def listnews(request):
    return HttpResponse("新闻信息列表。。。")

def listnews2(request):
    return HttpResponse("新闻信息列表2222。。。")