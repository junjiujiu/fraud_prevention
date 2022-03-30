import collections

from django.forms import model_to_dict as _model_to_dict
from django.http import JsonResponse as _JsonResponse


def success(data=None):
    """ Return a success response object """
    return _template_response(0, data)


def arguments_error():
    """ Return a arguments error response object """
    return _template_response(-1, msg='参数错误')


def permission_error():
    """ Return a permission error response object """
    return _template_response(-2, msg='没有权限')


def data_not_found_error():
    """ Return a data not found response object """
    return _template_response(-3, msg='数据未找到')


def data_exist_error():
    """ Return a data exist response object """
    return _template_response(-4, msg='数据已存在')


def url_error():
    """ Return a url error response object """
    return _template_response(-5, msg='请求链接错误')


def system_error():
    """ Return a system error response object """
    return _template_response(-6, msg='系统错误')


def _template_response(code, data=None, msg=''):
    """ Return a response object """
    if data:
        if isinstance(data, dict):
            json_data = data
        elif isinstance(data, collections.Iterable):
            json_data = []
            for o in data:
                json_data.append(_model_to_dict(o))
        else:
            json_data = _model_to_dict(data)
        data = json_data
    else:
        data = None
    return make_utf8_response({
        'code': code,
        'data': data,
        'msg': msg
    })


def make_utf8_response(json_body):
    """
    传入一个字典，返回一个json格式的http回复。
    确保response中的中文字符能够正常显示。
    """
    return _JsonResponse(json_body, json_dumps_params={'ensure_ascii':False})
