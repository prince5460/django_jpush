# _*_ coding: utf-8 _*_
# @Time : 2020/12/22 下午9:54
# @Author : zhou
# @File : signals.py
# @Desc :


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse

from .models import Article

from django_jpush.settings import app_key, master_secret

import jpush

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("INFO")


# 参数一接收哪种信号，参数二是接收哪个model的信号
@receiver(post_save, sender=Article, dispatch_uid="article_created")
def create_article(sender, instance=None, created=False, **kwargs):
    '''
    发布文章signals
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    '''
    print("hello world!")
    response = {}
    if created:
        try:
            article_create_notification(instance.title, instance.id)
        except Exception as e:
            response['msg'] = str(e)
            return JsonResponse(response)


def article_create_notification(title, article_id):
    '''
    文章发布notification
    :param title:
    :param article_id:
    :return:
    '''
    print("hello!")
    push = _jpush.create_push()

    push.audience = jpush.all_
    push.platform = jpush.all_

    ios = jpush.ios(alert="Hello, IOS JPush!", sound="a.caf", extras={'k1': 'v1'})
    android = jpush.android(alert="title:{},id:{}".format(title, article_id), priority=1, style=1, alert_type=1, )

    push.notification = jpush.notification(alert="Hello, JPush!", android=android, ios=ios)

    push.send()
