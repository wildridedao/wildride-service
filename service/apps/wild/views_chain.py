from .filters_chain import ChainFilter
from .models import Chain
from .serializers_chain import ChainSerializer, ChainCreateUpdateSerializer
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission


class ChainModelViewSet(CustomModelViewSet):
    """
    公链管理 的CRUD视图
    """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer  # 序列化器
    create_serializer_class = ChainCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = ChainCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = ChainFilter  # 过滤器
    # extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    # update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    # destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    # create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('F_ChainShort',)  # 搜索
    ordering = ['F_ID']  # 默认排序
