from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from django.db.models.fields import DecimalField, FloatField, IntegerField

from apps.wild.models.wild import Wild


class swapChar(models.Model):
    F_Tokenid = CharField(max_length=20, null=False,primary_key=True,verbose_name='主键')
    f_time = CharField(max_length=255, null=False,verbose_name='代币名称')
    # f_price = CharField(max_length=20, null=False,verbose_name='代币简称')
    timetype = CharField(max_length=20, null=True,verbose_name='时间类型')
    # f_amount = DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_small_in= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_small_out= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_small_sum= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_mid_in= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_mid_out= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_mid_sum= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_big_in= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_big_out= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_big_sum= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_count= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_count_in= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_count_out= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_price= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_price_in= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_price_out= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_in= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')
    f_swap_out= DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='')

    # F_Price= DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='当前价格')
    # F_Hisprice=DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='历史价格')
    class Meta:
        db_table='wild_tmp_time_swap'
        verbose_name = '主要交易信息汇总'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_Tokenid} 链"