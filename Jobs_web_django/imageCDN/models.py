from django.db import models


class ImageUrl(models.Model):
    TARGET = (
        ('0', '背景'),
        ('1', '头像'),
    )

    name = models.CharField(max_length=128, verbose_name='名字')
    url = models.CharField(max_length=256, verbose_name='地址')
    target = models.CharField(max_length=8, choices=TARGET, verbose_name='用途标记')
    class_target = models.CharField(max_length=8, default=0, verbose_name='分类标记')