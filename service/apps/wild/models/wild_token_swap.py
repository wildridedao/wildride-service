from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from django.db.models.fields import FloatField, IntegerField
from .token import Token


class Swap(models.Model):
    F_ID = CharField(max_length=20, null=False,unique=True,verbose_name='主键')
    F_Block= IntegerField(null=False,unique=True,verbose_name='所属区块')
    F_TimeStamp = IntegerField(null=False,verbose_name='时间戳（UTC时间）')
    F_From = CharField(max_length=50, null=False,verbose_name='交易账户')
    # F_SellerId= CharField(max_length=50, null=False,verbose_name='卖方TokenId')
    # F_BuyId = CharField(max_length=50, null=False,verbose_name='买方Tokenid')
    F_SellerId=ForeignKey(to='Token', on_delete=CASCADE, verbose_name="卖方TokenId", related_name='token_seller',
                      db_constraint=False,to_field="F_ID")
    F_BuyId=ForeignKey(to='Token', on_delete=CASCADE, verbose_name="买方Tokenid", related_name='token_buy',
                      db_constraint=False,to_field="F_ID")
    F_SellerAmount = FloatField(null=True,verbose_name='卖方数量')
    F_BuyAmount = FloatField( null=True,verbose_name='买方数量')
    F_Usd = FloatField( null=True,verbose_name='美元计价')
    F_Cny = FloatField( null=True,verbose_name='人民币计价')


    

    class Meta:
        db_table='wild_token_swap'
        verbose_name = 'swap交易'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_ID} 交易"