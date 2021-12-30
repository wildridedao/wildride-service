from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL


from vadmin.op_drf.models import CoreModel


# 继承框架封装的 模型类 CoreModel
class Chain(models.Model):
    F_ID = CharField(max_length=50, null=False, unique=True,verbose_name='ID主键' )
    F_ChainShort = CharField(max_length=10, null=False,verbose_name='公链简称')
    F_ChainName = CharField(max_length=30, null=False,verbose_name='公链名称')
    F_ScanSite = CharField(max_length=255, null=True, blank=True,verbose_name='区块浏览器网址')

    class Meta:
        db_table='wild_male_chain'
        verbose_name = '公链表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_ChainName} 链"