from django.urls import path,include

from applet.views import *

urlpatterns = [
    path('newslist/',listnews),
    path('news2/',listnews2)

]
