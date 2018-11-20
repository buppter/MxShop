"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from MxShop.settings import MEDIA_ROOT
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet, HotSearchsViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset
router = DefaultRouter()

# 配置goods的url
router.register('goods', GoodsListViewSet, base_name='goods')

# 配置category的url
router.register('categories', CategoryViewSet, base_name='categories')

# 发送短信验证码
router.register('code', SmsCodeViewset, base_name='code')

# 用户收藏
router.register('userfavs', UserFavViewset, base_name='userfavs')

# 用户
router.register('users', UserViewset, base_name='users')

# 热搜词
router.register('hotsearchs', HotSearchsViewset, base_name='hotsearchs')


urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # 富文本相关URL
    path('ueditor/', include('DjangoUeditor.urls')),

    # 商品列表页
    path('', include(router.urls)),


    path('docs/', include_docs_urls(title='慕学生鲜')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf自带的token模式
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口
    path('login/', obtain_jwt_token),


]
