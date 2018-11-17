from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    '''用户'''
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='', verbose_name='性别')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    email = models.CharField(max_length=20, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            # 如果不为空则返回用户名
            return self.name
        else:
            # 如果用户名为空则返回不能为空的对象
            return self.username


class MobileVerifyRecord(models.Model):
    code = models.CharField(max_length=50, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name='电话')
    # send_type = models.CharField(choices=(('register', '注册'), ('forget', '找回密码'), ('update_email', '修改手机号')),
    #                              max_length=20, verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}({1})".format(self.code, self.mobile)
