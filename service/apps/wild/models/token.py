from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from django.db.models.fields import DecimalField, FloatField, IntegerField

from apps.wild.models.wild import Wild


class Token(models.Model):
    F_ID = CharField(max_length=20, null=False,unique=True,primary_key=True,verbose_name='主键')
    # F_ChainId= CharField(max_length=50, null=False,verbose_name='所属公链')
    F_TokenName = CharField(max_length=255, null=False,verbose_name='代币名称')
    F_TokenShort = CharField(max_length=20, null=False,verbose_name='代币简称')
    # F_Contract= CharField(max_length=255, null=False,verbose_name='合约地址')
    F_Logo = CharField(max_length=255, null=False,verbose_name='logo地址')
    F_Total = FloatField(null=False,verbose_name='代币总量')
    F_Point = IntegerField(null=False,verbose_name='小数点')
    F_Holder = IntegerField(null=False,verbose_name='持有人数量')
    F_TransCount = IntegerField(null=False,verbose_name='转移次数')
    F_WebSite1= CharField(max_length=255, null=True,verbose_name='官方网站')
    F_Email = CharField(max_length=255, null=True,verbose_name='邮箱')
    F_Blog = CharField(max_length=255, null=True,verbose_name='博客')
    F_Twitter= CharField(max_length=255, null=True,verbose_name='Twitter')
    F_Telegram= CharField(max_length=255, null=True,verbose_name='Telegram')
    F_Discord= CharField(max_length=255, null=True,verbose_name='Discord')
    F_Cmc = CharField(max_length=255, null=True,verbose_name='cmc收录地址')
    F_Cg = CharField(max_length=255, null=True,verbose_name='cg收录地址')
    F_Fxh = CharField(max_length=255, null=True,verbose_name='非小号收录地址')
    F_Reddit = CharField(max_length=255, null=True,verbose_name='Reddit地址')
    F_Facebook= CharField(max_length=255, null=True,verbose_name='FB地址')
    F_Bitcointalk = CharField(max_length=255, null=True,verbose_name='Bitcointalk地址')
    F_Github = CharField(max_length=255, null=True,verbose_name='github地址')
    F_Github = CharField(max_length=255, null=True,verbose_name='github地址')
    # F_Hisprice=DecimalField(decimal_places='30',max_digits='65',null=True,verbose_name='历史价格')
    # F_Price=ForeignKey(to='Swap', on_delete=CASCADE, verbose_name="当前价格", related_name='project_dept',
    #                   db_constraint=False,to_field="F_ID")

    class Meta:
        db_table='wild_token'
        verbose_name = 'token表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_TokenName} 链"