from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from .models import Goods, GoodsCategory, HotSearchWords
from .serializer import GoodsSerializer, CategorySerializer, HotWordsSerializer
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    """
    自定义分页style
    """
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    商品列表页， 分页， 搜索， 过滤， 排序
    """
    queryset = Goods.objects.get_queryset().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """
    list:
    商品分类列表数据

    retrieve:
    商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer
