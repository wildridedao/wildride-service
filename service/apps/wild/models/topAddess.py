from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from django.db.models.fields import DecimalField, FloatField, IntegerField

from apps.wild.models.wild import Wild


class topAddess(models.Model):
    F_TokenAddress = CharField(max_length=255, null=False,primary_key=True,verbose_name='代币token')
    F_Address = CharField(max_length=255, null=False,verbose_name='钱包地址')
    F_TokenGroup = CharField(max_length=20, null=False,verbose_name='分片')
    F_Value = DecimalField(decimal_places=18,max_digits=65,max_length=255, null=True,verbose_name='持币总量')
    # F_Price= DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='当前价格')
    # F_Hisprice=DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='历史价格')
    
    class Meta:
        db_table='wild_balance'
        verbose_name = '持币分析'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_TokenAddress} 链"