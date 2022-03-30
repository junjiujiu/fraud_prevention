from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from applet.models import News
from applet.utils import response_utils


@require_http_methods(["GET"])
def news(request, news_id=None):
    if request.method == 'GET':
        news = News.objects.filter(pk=news_id)
        if news:
            return response_utils.success(news)
        else:
            return response_utils.data_not_found_error()
