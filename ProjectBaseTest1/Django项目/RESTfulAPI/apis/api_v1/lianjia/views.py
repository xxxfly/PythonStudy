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
        print(request.body)
        param = dict()
        param['sign'] = request.POST.get('sign', '')
        param['page_size'] = request.POST.get('page_size', 10)
        param['page_index'] = request.POST.get('page_index', 1)
        param['search_condition'] = request.POST.get('search_condition', '[]')
        param['selected_condition'] = request.POST.get('selected_condition', '[]')

        serializer = serializers.GetCJPageListSerializer(data=param)
        if serializer.is_valid():
            result = serializer.get_list(serializer.validated_data)
            return Response(result, status=status.HTTP_201_CREATED, content_type='application/json,charset=utf-8')
        else:
            return Response(dict(error_code=ErrorCode.参数错误.value, error=json.dumps(serializer.errors, ensure_ascii=False)),
                     status=status.HTTP_400_BAD_REQUEST)
