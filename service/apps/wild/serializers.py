from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.request import Request
from apps.wild.models.KChar import KChar
from apps.wild.models.wild_token_swap_char import swapChar
from .models import Wild,TokenDetail,Tokenlist,topAddess
from .models import Token,Liquidity,Swap,Transfer
from vadmin.op_drf.serializers import CustomModelSerializer


# ================================================= #
# ************** 项目管理 序列化器  ************** #
# ================================================= #
class WildSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Wild
        fields = '__all__'


class WildCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Wild
        fields = '__all__'


class ExportProjectSerializer(CustomModelSerializer):
    """
    导出 项目管理 简单序列化器
    """
    person__username = serializers.SerializerMethodField(read_only=False)
    dept__deptName = serializers.SerializerMethodField(read_only=False)

    def get_person__username(self, obj):
        return "" if not hasattr(obj, 'person') else obj.person.username

    def get_dept__deptName(self, obj):
        return "" if not hasattr(obj, 'dept') else obj.dept.deptName

    class Meta:
        model = Wild
        fields = ('id', 'name', 'code', 'person', 'person__username', 'dept', 'dept__deptName', 'creator', 'modifier',
                  'description')
# ================================================= #
# ************** Token 序列化器  ************** #
# ================================================= #
class TokenSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """
    class Meta:
        model = Token
        fields = '__all__'
        
class TokenCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Token
        fields = '__all__'

# ================================================= #
# ************** Liquidity 序列化器  ************** #
# ================================================= #
class LiquiditySerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Liquidity
        fields = '__all__'
        
class LiquidityCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Liquidity
        fields = '__all__'

# ================================================= #
# ************** Swap 序列化器  ************** #
# ================================================= #
class SwapSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Swap
        fields = '__all__'
        
class SwapCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Swap
        fields = '__all__'

# ================================================= #
# ************** Liquidity 序列化器  ************** #
# ================================================= #
class TransferSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Transfer
        fields = '__all__'
        
class LTransferCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Transfer
        fields = '__all__'

# ================================================= #
# ************** Liquidity 序列化器  ************** #
# ================================================= #
class TokenlistSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Tokenlist
        fields = '__all__'
        
class TokenlistCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Tokenlist
        fields = '__all__'

# ================================================= #
# ************** KChar 序列化器  ************** #
# ================================================= #
class KCharSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = KChar
        fields = '__all__'
        
class KCharCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = KChar
        fields = '__all__'
        
# ================================================= #
# ************** TokenDetail 序列化器  ************** #
# ================================================= #
class TokenDetailSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = TokenDetail
        fields = '__all__'
        
class TokenDetailCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = TokenDetail
        fields = '__all__'
# ================================================= #
# ************** swapChar 序列化器  ************** #
# ================================================= #
class swapCharSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = swapChar
        fields = '__all__'
        
class swapCharCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = swapChar
        fields = '__all__'
        
# ================================================= #
# ************** topAddess 序列化器  ************** #
# ================================================= #
class topAddessSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = topAddess
        fields = '__all__'

class topAddessCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = topAddess
        fields = '__all__'