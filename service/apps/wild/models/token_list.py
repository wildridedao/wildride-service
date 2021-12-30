from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from django.db.models.fields import DecimalField, FloatField, IntegerField

from apps.wild.models.wild import Wild


class Tokenlist(models.Model):
    F_ID = CharField(max_length=20, null=False,primary_key=True,verbose_name='主键')
    F_TokenName = CharField(max_length=255, null=False,verbose_name='代币名称')
    F_TokenShort = CharField(max_length=20, null=False,verbose_name='代币简称')
    F_Total = DecimalField(decimal_places=30,max_digits=64,max_length=255, null=True,verbose_name='代币总量')
    F_Price= DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='当前价格')
    F_Hisprice=DecimalField(decimal_places=30,max_digits=64,max_length=255,null=True,verbose_name='历史价格')
    class Meta:
        db_table='token_list'
        verbose_name = 'token列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_TokenName} 链"