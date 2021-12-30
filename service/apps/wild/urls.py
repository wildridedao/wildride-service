from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import AllKCharModelViewSet, DayKCharModelViewSet, MonKCharModelViewSet, SwapCharModelViewSet, TokenDetailModelViewSet, TokenlistModelViewSet, WekKCharModelViewSet, WildModelViewSet,TokenModelViewSet,LiquidityModelViewSet,SwapModelViewSet,TransferModelViewSet, YeaKCharModelViewSet, topAddessModelViewSet,KCharModelViewSet
from .views_chain import ChainModelViewSet

router = DefaultRouter()
# print("1/////////////////")
print(router.urls)

# router.register(r'project1', WildModelViewSet)
router.register(r'male/chain', ChainModelViewSet)

print(router.urls)

router.register(r'token', TokenModelViewSet)
router.register(r'Liquidity', LiquidityModelViewSet)
router.register(r'Swap', SwapModelViewSet)
router.register(r'Transfer', TransferModelViewSet)
router.register(r'Tokenlist', TokenlistModelViewSet)
router.register(r'KChars', KCharModelViewSet)
router.register(r'KChar/day', DayKCharModelViewSet)
router.register(r'KChar/week', WekKCharModelViewSet)
router.register(r'KChar/month', MonKCharModelViewSet)
router.register(r'KChar/year', YeaKCharModelViewSet)
router.register(r'KChar/all', AllKCharModelViewSet)
router.register(r'Tokendatail', TokenDetailModelViewSet)
router.register(r'SwapChar', SwapCharModelViewSet)
router.register(r'TopAddess', topAddessModelViewSet)


# urlpatterns = [
#     # 导出项目
#     re_path('project/export/', ChainModelViewSet.as_view({'get': 'export', })),
#     # 项目导入模板下载及导入
#     re_path('project/importTemplate/',
#             ChainModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
# ]
# print("3/////////////////")
print(router.urls)
# print("/////////////////")
urlpatterns = router.urls