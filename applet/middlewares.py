from django.utils.deprecation import MiddlewareMixin
from applet.utils import response_utils
from fraud_prevention.urls import APPLET_API_PREFIX


# 处理全局异常，目前只捕捉applet/api的异常
class ExceptionMiddleware(MiddlewareMixin):
    # 如果注册多个process_exception函数，那么函数的执行顺序与注册的顺序相反。(其他中间件函数与注册顺序一致)
    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        if APPLET_API_PREFIX in request.path_info:
            print(request, exception)
            return response_utils.system_error()
