# -*- coding: utf-8 -*-
import json

_Author_ = 'BUPPT'

from django.views.generic.base import View
from .models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过Django的View实现的商品列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dice = {}
        #     json_dice['name'] = good.name
        #     json_dice['goods_sn'] = good.goods_sn
        #     json_dice['category'] = good.category.name
        #     json_dice['market_price'] = good.market_price
        #     json_list.append(json_dice)

        # from django.forms.models import model_to_dict
        #
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        return JsonResponse(json_data, safe=False)