from django.conf import settings
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL
from django.db.models.fields import FloatField, IntegerField


class Transfer(models.Model):
    F_ID = CharField(max_length=66, null=False,unique=True,primary_key=True,verbose_name='主键')
    F_TokenId= CharField(max_length=50, null=False,unique=True,verbose_name='token主键')
    F_From = CharField(max_length=50, null=False,verbose_name='发送方')
    F_Recipient = CharField(max_length=50, null=False,verbose_name='接收方')
    F_Amount= FloatField(null=True,verbose_name='数量')
    F_TimeStamp = IntegerField( null=False,verbose_name='时间戳（utc时间）')
    F_Block = IntegerField(null=True,verbose_name='所属区块')


    

    class Meta:
        db_table='wild_token_transfer'
        verbose_name = '转账交易'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.F_TokenId} 交易"