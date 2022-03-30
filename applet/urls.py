from django.urls import path,include

from applet.views import *

urlpatterns = [
    # 用户接口

    # 新闻接口
    path('news/<int:news_id>', news),
    path('news/', create_news),
    path('news/recentNews', recent_news),


]
