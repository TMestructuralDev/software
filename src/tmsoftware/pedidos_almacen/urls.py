from django.urls import path
from .views import IngenieroList, MaterialList, PedidoList, PedidoMaterialList

urlpatterns = [
    path('ingenieros/', IngenieroList.as_view(), name='ingeniero-list'),
    path('materiales/', MaterialList.as_view(), name='material-list'),
    path('pedidos/', PedidoList.as_view(), name='pedido-list'),
    path('pedidos-materiales/', PedidoMaterialList.as_view(), name='pedido-material-list'),
]