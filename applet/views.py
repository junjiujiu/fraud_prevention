from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from applet.models import News


@require_http_methods(["GET"])
def news(request, news_id=None):
    if request.method == 'GET':
        news = News.objects.get(pk=news_id)
        if news:
            return JsonResponse(model_to_dict(news))
        else:
            # TODO:定义数据返回的通用类,目前这里不会执行，会在get时就报错
            return JsonResponse({'code':-1})