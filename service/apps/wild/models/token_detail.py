from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from django.db.models.fields import DecimalField, FloatField, IntegerField

from apps.wild.models.wild import Wild


class TokenDetail(models.Model):
    f_id = CharField(max_length=20, null=False,unique=True,primary_key=True,verbose_name='主键')
    F_TokenName = CharField(max_length=255, null=False,verbose_name='代币名称')
    F_TokenShort = CharField(max_length=20, null=False,verbose_name='代币简称')
    F_Total = DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='代币总量')
    F_Price= DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='当前价格')
    maxprice=DecimalField(decimal_places=30,max_digits=64,verbose_name='最高价')
    minprice = DecimalField(decimal_places=30,max_digits=64,verbose_name='最低价')
    wave = FloatField(verbose_name='波动')
    amount= DecimalField(decimal_places=30,max_digits=64,null=True,verbose_name='交易量')
    amountprice = DecimalField(decimal_places=18,max_digits=65,null=True,verbose_name='交易额')
    allamountprice = DecimalField(decimal_places=18,max_digits=65,null=True,verbose_name='总市值')
    changprice =DecimalField(decimal_places=30,max_digits=64,null=True,verbose_name='换手')
    F_Hisprice=DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='历史价格')
    islist= CharField(max_length=2, null=False,verbose_name='列表是否显示')
    f_addwave=DecimalField(decimal_places=5,max_digits=20,verbose_name='涨跌幅')
    f_count=DecimalField(decimal_places=5,max_digits=20,verbose_name='交易次数')
    
    class Meta:
        db_table='wild_tmp_token_detail'
        verbose_name = 'token表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_TokenName} 链"