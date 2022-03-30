from applet.models import Redis
import datetime


def exist(key: str) -> bool:
    o = Redis.objects.filter(mkey__exact=key).first()
    if o:
        return True
    else:
        return False


def delete(key: str) -> bool:
    o = Redis.objects.filter(mkey__exact=key).first()
    if o:
        o.delete()
        return True
    else:
        return False


def ttl(key: str) -> int:
    o = Redis.objects.filter(mkey__exact=key).first()
    if o:
        return int((o.expireTime-datetime.datetime.now()).total_seconds())
    else:
        return 0


def set_in_seconds(key: str, value, in_time_seconds):
    expire_datatime = datetime.datetime.now() + datetime.timedelta(seconds=in_time_seconds)
    set_before_datetime(key, value, expire_datatime)


def set_before_datetime(key: str, value, expire_datetime):
    o = Redis.objects.filter(mkey__exact=key).first()
    if o:
        # 更新现有的
        o.content = value
        o.expireTime = expire_datetime
        o.save()
    else:
        # 新建一个记录
        o = Redis(
            mkey=key,
            content=value,
            expireTime=expire_datetime
        )
        o.save()


def get_available_content(key: str):
    o = Redis.objects.filter(mkey__exact=key).first()
    if o:
        # 十秒内算过期
        if ttl(key) >= 10:
            return o.content
    return None
