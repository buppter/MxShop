from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import ShoppingCart
from goods.models import Goods


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    goods_num = serializers.IntegerField(required=True, min_value=1, label="数量",
                                    error_messages={
                                        'min_value': "商品数量不得小于1",
                                        'required': "请选择商品数量",
                                    })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all(), label="商品")

    def create(self, validated_data):
        user = self.context["request"].user
        goods_num = validated_data["goods_num"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.goods_num += goods_num
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed
