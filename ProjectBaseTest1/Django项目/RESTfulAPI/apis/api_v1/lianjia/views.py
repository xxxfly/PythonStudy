# -*- coding: utf-8

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from ..enum import ErrorCode


@api_view(['POST'])
def cjlist(request):
    """
    POST：获取列表信息
    """
    if request.method == 'POST':
        parm = dict()
        parm['sign'] = request.POST.get('sign', None)
        parm['pageSize'] = request.POST.get('pageSize', 10)
        parm['pageIndex'] = request.POST.get('pageIndex', 1)
        parm['searchCondition'] = request.POST.get('searchCondition', [])
        parm['selectedCondition'] = request.POST.get('selectedCondition', [])
        serializer = serializers.GetCJPageListSerializer(data=parm)
        if serializer.is_valid():
            result = serializer.get_list(serializer.validated_data)
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            Response(dict(error_code=ErrorCode.参数错误.value, error=json.dumps(serializer.errors, ensure_ascii=False)),
                     status=status.HTTP_400_BAD_REQUEST)