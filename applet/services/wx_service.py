import requests
from applet.services import redis_service


def _code2Session(code):
    appid = redis_service.get_available_content('appid')
    secret = redis_service.get_available_content('secret')
    if appid and secret:
        request_url = 'https://api.weixin.qq.com/sns/jscode2session'
        url_params = {
            'appid':appid,
            'secret':secret,
            'js_code':code,
            'grant_type':'authorization_code'
        }
        response = requests.get(request_url, params=url_params)
        response.raise_for_status()
        res_json = response.json()
        error_code = res_json.get('errcode', 0)
        if error_code == 0:
            # 请求成功
            return res_json
        else:
            return None


def get_openid(code):
    wx_json = _code2Session(code)
    if wx_json:
        return wx_json['openid']
    return None

