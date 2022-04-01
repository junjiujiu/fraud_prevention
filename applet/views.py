from django.http import QueryDict
from django.views.decorators.http import require_http_methods, require_POST

from applet.models import News, AssessMessage, User
from applet.services import sms_service, wx_service
from applet.utils import response_utils


@require_http_methods(['POST'])
def login(request):
    code = request.POST.get('code', None)
    if code:
        openid = wx_service.get_openid(code)
        u = User.objects.filter(openid__exact=openid).first()
        if u:
            return response_utils.success({'userid': u.id})
        else:
            return response_utils.data_not_found_error()
    else:
        return response_utils.arguments_error()


@require_http_methods(['POST'])
def create_user(request):
    data = request.POST
    code = data.get('code', None)
    username = data.get('userName', None)
    avatar_url = data.get('avatarUrl', None)
    if code and username and avatar_url:
        openid = wx_service.get_openid(code)
        u = User.objects.filter(openid__exact=openid)
        if u:
            return response_utils.data_exist_error()
        else:
            u = User(
                openid=openid,
                userName=username,
                avatarUrl=avatar_url
            )
            u.save()
            return response_utils.success(u)
    else:
        return response_utils.arguments_error()


@require_http_methods(['GET', 'PUT'])
def user(request, id):
    # 先统一获取用户信息
    u = User.objects.filter(pk=id).first()
    if not u:
        return response_utils.data_not_found_error()

    if request.method == 'GET':
        return response_utils.success(u)

    elif request.method == 'PUT':
        data = QueryDict(request.body)
        swindle_num = data.get('swindledNum', None)
        if swindle_num:
            u.swindledNum = swindle_num
            u.save()
            return response_utils.success()
        else:
            return response_utils.arguments_error()
    else:
        return response_utils.permission_error()


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
        percentage = sms_service.calculate_insecurity_percentage(message)
        percentage = max(min(percentage, 100), 0)  # 属于[0,100]
        sms = AssessMessage(
            userid=user_id,
            messageInfo=message,
            percentage=percentage  # 传入是诈骗短信的概率
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
