from django.db import models


class ChatInformation(models.Model):
    id = models.IntegerField('数据编号', primary_key=True)
    usrid = models.CharField('用户编号', max_length=50, default='')
    date = models.DateTimeField('时间戳')
    content = models.CharField('聊天内容', max_length=50, default='')