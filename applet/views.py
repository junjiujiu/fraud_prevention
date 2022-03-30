from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods, require_POST

from applet.models import News, AssessMessage
from applet.services import sms_service
from applet.utils import response_utils

@require_http_methods(['POST'])
def login(request):
    pass

@require_http_methods(['POST'])
def create_user(request):
    pass

@require_http_methods(['GET','PUT'])
def user(request, id):
    if request.method == 'PUT':
        swindledNum = request.PUT.get('swindledNum', None)



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
    try:
        n = News(
            title=data['title'],
            content=data['content'],
            createTime=data['createTime'],
            source=data['source'],
            type=data['type']
        )
    except Exception as e:
        return response_utils.arguments_error()
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


@require_http_methods(['POST'])
def recognition(request):
    data = request.POST
    user_id = data.get('userid', None)
    message = data.get('messageInfo', None)
    if user_id and message:
        percentage = sms_service.calculate_safe_percentage(message)
        sms = AssessMessage(
            userid=user_id,
            messageInfo=message,
            percentage=1-percentage  # 传入是诈骗短信的概率
        )
        sms.save()
        return response_utils.success({'percentage': percentage})
    else:
        return response_utils.arguments_error()


@require_http_methods(['GET'])
def user_messages(request):
    user_id = request.GET.get('userid', None)
    if user_id:
        result_data = AssessMessage.objects.filter(userid__exact=user_id)
        return response_utils.success(result_data)
    else:
        return response_utils.arguments_error()


