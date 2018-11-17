# -*- coding: utf-8 -*-
_Author_ = 'BUPPT'

import xadmin
from xadmin import views
from .models import MobileVerifyRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学生鲜后台"
    site_footer = "mxshop"
    menu_style = "accordion"


class MobileVerifyRecordAdmin(object):
    list_display = ['code', 'mobile', "send_time"]
    model_icon = 'fa fa-check-square'


xadmin.site.register(MobileVerifyRecord, MobileVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)