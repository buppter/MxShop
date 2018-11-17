from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters

from .models import Goods, GoodsCategory
from .serializer import GoodsSerializer, CategorySerializer
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    """
    自定义分页style
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    商品列表页， 分页， 搜索， 过滤， 排序
    """
    queryset = Goods.objects.get_queryset().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """
    List:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
