from django.urls import path

from applet.views import *

USER_PREFIX = 'user'
NEWS_PREFIX = 'news'
SMS_PREFIX = 'recognition'

urlpatterns = [
    # 用户接口
    path(USER_PREFIX+'/login', login),  # code登录
    path(USER_PREFIX+'/', create_user),  # POST注册、GET根据openid获取用户信息
    path(USER_PREFIX+'/<int:id>', user),  # GET根据id获取信息、PUT修改被骗指数

    # 新闻接口
    path(NEWS_PREFIX+'/<int:news_id>', news),
    path(NEWS_PREFIX+'/', create_news),
    path(NEWS_PREFIX+'/recentNews', recent_news),

    # 短信接口
    path(SMS_PREFIX+'/', recognition),
    path(SMS_PREFIX+'/userhas', user_messages)

]
