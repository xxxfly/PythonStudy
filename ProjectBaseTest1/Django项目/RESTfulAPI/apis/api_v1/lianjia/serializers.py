# -*- coding: utf-8
from rest_framework import serializers
from apps.lianjia.models import whlianjiachengjiao
from ..enum import ErrorCode
from ..base import BaseApi
from django.core.serializers import serialize


class GetCJPageListSerializer(serializers.Serializer):
    """
    获取列表信息
    """
    sign = serializers.CharField(max_length=150)
    page_size = serializers.IntegerField()
    page_index = serializers.IntegerField()
    search_condition = serializers.CharField()
    selected_condition = serializers.CharField()

    def get_list(self, validated_data):
        result = dict()

        base_api = BaseApi()
        # 验证接口加密信息
        sign = validated_data['sign']

        # 获取数据
        try:
            page_size = validated_data['page_size']  # 分页大小
            page_index = validated_data['page_index']  # 当前页码
            search_condition_list = eval(validated_data['search_condition'])  # 搜索条件列表
            selected_condition_list = eval(validated_data['selected_condition'])  # 选择条件列表

            searchName = search_condition_list[0]
            whlianjiachengjiao_list = whlianjiachengjiao.objects.all().order_by('dealDate')
            if searchName != '' and searchName != None:
                whlianjiachengjiao_list = whlianjiachengjiao_list.filter(title__contains=searchName)

            total_count = whlianjiachengjiao_list.count()
            page_number = total_count // page_size + 1

            whlianjiachengjiao_list = whlianjiachengjiao_list[(page_index-1)*page_size:page_index*page_size+1]

            result["dataList"] = serialize('json',  whlianjiachengjiao_list, ensure_ascii=False)
            result["totalCount"] = total_count
            result["pageNumber"] = page_number
            result["error_code"] = ErrorCode.正确.value
            result["error"] = ""
            return result

        except Exception as ex:
            print('-------error--------')
            print(ex)
            result['dataList'] = '[]'
            result["totalCount"] = 0
            result["pageNumber"] = 0
            result["error_code"] = ErrorCode.操作错误.value
            result["error"] = "查询出错"
            return result
