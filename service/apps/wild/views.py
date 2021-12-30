from apps.wild.models import topAddess
from .filters import KCharFilter, TokenlistFilter, WildFilter,TokenFilter,TransferFilter,LiquidityFilter,SwapFilter,TokenDetailFilter, swapCharFilter, topAddessFilter
from .models import Wild,Token,Liquidity,Swap,Transfer,KChar,Tokenlist,TokenDetail,swapChar
from .serializers import ExportProjectSerializer, KCharSerializer,TokenSerializer,TokenCreateUpdateSerializer, TokenlistSerializer,WildSerializer,WildCreateUpdateSerializer,TokenDetailSerializer, swapCharSerializer, topAddessSerializer
from .serializers import TransferSerializer,SwapSerializer,LiquiditySerializer
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission
import time;


class WildModelViewSet(CustomModelViewSet):
    """
    Token管理 的CRUD视图
    """
    queryset = Wild.objects.all()
    serializer_class = WildSerializer  # 序列化器
    create_serializer_class = WildCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = WildCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = WildFilter  # 过滤器
    # extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    # update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    # destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    # create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('name',)  # 搜索
    ordering = ['create_datetime']  # 默认排序
    # 导出
    export_field_data = ['项目序号', '项目名称', '项目编码', '项目负责人', '项目所属部门', '创建者', '修改者', '备注']  # 导出
    export_serializer_class = ExportProjectSerializer  # 导出序列化器
    # 导入
    import_field_data = {'name': '项目名称', 'code': '项目编码', 'person': '项目负责人ID', 'dept': '部门ID'}
    import_serializer_class = ExportProjectSerializer

class TokenModelViewSet(CustomModelViewSet):
    """
    Token管理 的CRUD视图
    """
    queryset = Token.objects.all()
    serializer_class = TokenSerializer  # 序列化器
    create_serializer_class = TokenCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = TokenCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = TokenFilter  # 过滤器
    search_fields = ('F_TokenName',)  # 搜索
    ordering = ['F_ID']  # 默认排序


class TransferModelViewSet(CustomModelViewSet):
    """
    Transfer管理 的CRUD视图
    """
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer  # 序列化器
    filter_class =  TransferFilter  # 过滤器
    search_fields = ('F_ID',)  # 搜索
    ordering = ['F_ID']  # 默认排序

class SwapModelViewSet(CustomModelViewSet):
    """
    Swap管理 的CRUD视图
    """
    queryset = Swap.objects.all()
    serializer_class = SwapSerializer  # 序列化器
    filter_class =  SwapFilter  # 过滤器
    search_fields = ('F_ID',)  # 搜索
    ordering = ['F_ID']  # 默认排序

class LiquidityModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
    queryset = Liquidity.objects.all()
    serializer_class = LiquiditySerializer  # 序列化器
    filter_class =  LiquidityFilter  # 过滤器
    search_fields = ('F_ID',)  # 搜索
    ordering = ['F_ID']  # 默认排序


class TokenlistModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
    queryset = Tokenlist.objects.all()
    serializer_class = TokenlistSerializer  # 序列化器
    filter_class =  TokenlistFilter  # 过滤器
    search_fields = ('F_ID',)  # 搜索
     # 默认排序

class KCharModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
 
    queryset = KChar.objects.all()
    serializer_class = KCharSerializer  # 序列化器
    filter_class = KCharFilter  # 过滤器


class DayKCharModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
    # edate = time.time()-(60*60*24*365)
    # sdate= time.time()-(60*60*24*366)
    queryset = KChar.objects.all().filter(timetype='min5')
    serializer_class = KCharSerializer  # 序列化器
    filter_class = KCharFilter  # 过滤器


class WekKCharModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
    edate = time.time()
    sdate= time.time()-(60*60*24*7)
    queryset = KChar.objects.all().filter(f_time__gt=sdate,f_time__lt=edate,timetype='min55')
    serializer_class = KCharSerializer  # 序列化器
    filter_class = KCharFilter  # 过滤器


class MonKCharModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
    edate = time.time()
    sdate= time.time()-(60*60*24*30)
    queryset = KChar.objects.all().filter(f_time__gt=sdate,f_time__lt=edate,timetype='h2')
    serializer_class = KCharSerializer  # 序列化器
    filter_class = KCharFilter  # 过滤器


class YeaKCharModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
    edate = time.time()
    sdate= time.time()-(60*60*24*365)
    queryset = KChar.objects.all().filter(f_time__gt=sdate,f_time__lt=edate,timetype='d1')
    serializer_class = KCharSerializer  # 序列化器
    filter_class = KCharFilter  # 过滤器


class AllKCharModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
   
    queryset = KChar.objects.all().filter(timetype='d1')
    serializer_class = KCharSerializer  # 序列化器
    filter_class = KCharFilter  # 过滤器
 

class TokenDetailModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
   
    queryset = TokenDetail.objects.all().filter(islist='1')
    serializer_class = TokenDetailSerializer  # 序列化器
    filter_class = TokenDetailFilter  # 过滤器
    search_fields = ('t_id',)  # 搜索

class SwapCharModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
   
    queryset = swapChar.objects.all()
    serializer_class = swapCharSerializer  # 序列化器
    filter_class = swapCharFilter  # 过滤器
    search_fields = ('t_id',)  # 搜索
    
class topAddessModelViewSet(CustomModelViewSet):
    """
    Liquidity管理 的CRUD视图
    """
   
    queryset = topAddess.objects.all().filter(F_TokenGroup='1')
    serializer_class = topAddessSerializer  # 序列化器
    filter_class = topAddessFilter  # 过滤器
    search_fields = ('t_id',)  # 搜索