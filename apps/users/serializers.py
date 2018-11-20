import re
from datetime import datetime, timedelta

from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
from MxShop.settings import REGEX_MOBILE
from .models import MobileVerifyRecord


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if MobileVerifyRecord.objects.filter(send_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户注册
    """
    code = serializers.CharField(max_length=4, min_length=4, required=True, help_text="验证码", label="验证码",
                                 write_only=True,
                                 error_messages={
                                     "required": "请输入验证码",
                                     "blank": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 })

    username = serializers.CharField(required=True, allow_blank=False, min_length=5, label="用户名",
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")],
                                     error_messages={
                                         "blank": "用户名不能为空",
                                         "required": "用户名不能为空",
                                         "min_length": "用户名长度不能小于5位"
                                     })
    password = serializers.CharField(style={'input_type': 'password'}, label="密码", write_only=True)

    # 对密码进行加密
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    # 判断验证码
    def validate_code(self, code):
        verify_records = MobileVerifyRecord.objects.filter(mobile=self.initial_data["username"]).order_by('-send_time')
        if verify_records:
            last_record = verify_records[0]

            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)

            if five_minutes_ago > last_record.send_time:
                raise serializers.ValidationError("验证码过期")
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["mobile"] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "password", "mobile")
