from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from utils.permissions import IsOwnerOrReadOnly
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer


class ShoppingCartViewset(viewsets.ModelViewSet):
    """
    购物车功能开发
    list:
    获取购物车详情

    create:
    加入购物车

    delete:
    删除购物车

    update:
    更新购物车列表
    """
    serializer_class = ShoppingCartSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    queryset = ShoppingCart.objects.all()
