import django_filters
from apps.wild.models.KChar import KChar
from apps.wild.models.token_detail import TokenDetail
from apps.wild.models.wild_token_swap_char import swapChar


from .models import Wild
from .models import Token
from .models import Liquidity
from .models import Swap
from .models import Transfer
from .models import Tokenlist,topAddess



class WildFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Wild
        exclude = ()


class TokenFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Token
        exclude = ()

class LiquidityFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Liquidity
        exclude = ()

class SwapFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Swap
        exclude = ()

class TransferFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Transfer
        exclude = ()

class TokenlistFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tokenlist
        exclude = ()

class KCharFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = KChar
        exclude = ()

class TokenDetailFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='F_TokenShort')
    class Meta:
        model = TokenDetail
        exclude = ()

class swapCharFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = swapChar
        exclude = ()

class topAddessFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = topAddess
        exclude = ()