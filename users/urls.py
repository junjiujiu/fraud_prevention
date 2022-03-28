from django.urls import path,include

from users.views import *

urlpatterns = [
    path('newslist/',listnews),
    path('news2/',listnews2)

]
