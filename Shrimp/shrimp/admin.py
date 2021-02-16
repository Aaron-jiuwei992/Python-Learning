from django.contrib import admin
# 导出AdminSite类
from django.contrib.admin import AdminSite

from . import models

# 定义ShrimAdmin的子类型
class ShrimpAdmin(admin.ModelAdmin):
    pass

# 对AdminSite进行子类化，并覆盖其属性
class ShrimpAdminSite(AdminSite):
    site_title = '虾问'
    site_header = '虾问后台管理系统'
    index_title = '虾问后台首页'


shrimp_admin_site = ShrimpAdminSite(name='shrim')
# 通过AdminSite对象的register方法进行模型注册
shrimp_admin_site.register(models.User, ShrimpAdmin)
shrimp_admin_site.register(models.UrlToken, ShrimpAdmin)
shrimp_admin_site.register(models.Question, ShrimpAdmin)
shrimp_admin_site.register(models.Answer, ShrimpAdmin)