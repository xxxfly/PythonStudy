# -*- coding: utf-8

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from ..enum import ErrorCode


@api_view(['GET', 'POST'])
def user(request):
    """
    GET：获取用户信息
    POST：更新用户信息
    """
    if request.method == 'GET':
        print('GET')
        param = dict()
        param['token'] = request.GET.get("token", None)
        param['user_id'] = request.GET.get("user_id", 0)
        serializer = GetUserSerializer(data=param)
        if serializer.is_valid():
            result = serializer.get_user(serializer.validated_data)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(dict(error_code=ErrorCode.参数错误.value, error=json.dumps(serializer.errors, ensure_ascii=False)),
                        status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        param = dict()
        param['token'] = request.POST.get("token", None)
        param['user_guid'] = request.POST.get("user_guid", None)
        param['user_name'] = request.POST.get("user_name", None)
        param['real_name'] = request.POST.get("real_name", None)
        param['mobile'] = request.POST.get("mobile", None)
        param['balance'] = request.POST.get("balance", 0)
        param['available_balance'] = request.POST.get("available_balance", 0)
        serializer = AddUserSerializer(data=param)
        if serializer.is_valid():
            result = serializer.add_user(serializer.validated_data)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(dict(error_code=ErrorCode.参数错误.value, error=json.dumps(serializer.errors, ensure_ascii=False)),
                        status=status.HTTP_400_BAD_REQUEST)
