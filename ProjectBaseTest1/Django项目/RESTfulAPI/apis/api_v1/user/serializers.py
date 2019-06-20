# -*- coding: utf-8
from rest_framework import serializers
from apps.user.models import User
from ..enum import ErrorCode
from ..base import BaseApi


class GetUserSerializer(serializers.Serializer):
    """
    获取用户信息
    """
    token = serializers.CharField(max_length=150)
    user_id = serializers.IntegerField()


    def get_user(self, validated_data):
        result = dict()
        base_api = BaseApi()
        # 获取用户
        try:
            user = User.objects.get(user_id=validated_data['user_id'])
        except User.DoesNotExist:
            result["error_code"] = ErrorCode.用户不存在.value
            result["error"] = "用户不存在"
            return result
        # 认证

        result["nick_name"] = user.user_name
        result["avatar"] = user.avatar
        result["error_code"] = ErrorCode.正确.value
        result["error"] = ""
        return result


class AddUserSerializer(serializers.Serializer):
    """
    新增用户
    """
    token = serializers.CharField(max_length=150)
    user_guid = serializers.CharField(max_length=150)
    user_name = serializers.CharField(max_length=100)
    real_name = serializers.CharField(max_length=100)
    mobile = serializers.CharField(max_length=50)
    balance = serializers.DecimalField(max_digits=8, decimal_places=2)
    available_balance = serializers.DecimalField(max_digits=8, decimal_places=2)

    def add_user(self, validated_data):
        result = dict()
        print(validated_data)
        # 新增用户
        try:
            new_user = User(
                user_guid=validated_data['user_guid'],
                user_name=validated_data['user_name'],
                real_name=validated_data['real_name'],
                mobile=validated_data['mobile'],
                balance=validated_data['balance'],
                available_balance=validated_data['available_balance']
            )
            new_user.save()

        except Exception as ex:
            print('--------------------')
            print(ex)
            print('--------------------')
            result["error_code"] = ErrorCode.用户不存在.value
            result["error"] = ''
            return result

        result["error_code"] = ErrorCode.正确.value
        result["error"] = ""
        return result
