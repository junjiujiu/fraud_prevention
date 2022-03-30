from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods, require_POST

from applet.models import News
from applet.utils import response_utils


@require_http_methods(['GET'])
def news(request, news_id=None):
    if request.method == 'GET':
        result = News.objects.filter(pk=news_id)
        if result:
            return response_utils.success(result)
        else:
            return response_utils.data_not_found_error()


@require_http_methods(['POST'])
def create_news(request):
    data = request.POST
    n = News(
        title=data['title'],
        content=data['content'],
        createTime=data['createTime'],
        source=data['source'],
        type=data['type']
    )
    n.save()
    return response_utils.success()


@require_http_methods(['GET'])
def recent_news(request):
    news_type = request.GET.get('type', None)
    if news_type:
        result_data = News.objects.filter(type__exact=news_type)
        return response_utils.success(result_data)
    else:
        return response_utils.arguments_error()
