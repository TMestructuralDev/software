from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingeniero, Material, Pedido, PedidoMaterial
from .serializers import IngenieroSerializer, MaterialSerializer, PedidoSerializer, PedidoMaterialSerializer

class IngenieroList(APIView):
    def get(self, request):
        ingenieros = Ingeniero.objects.all()
        serializer = IngenieroSerializer(ingenieros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngenieroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaterialList(APIView):
    def get(self, request):
        materiales = Material.objects.all()
        serializer = MaterialSerializer(materiales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PedidoList(APIView):
    def get(self, request):
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PedidoMaterialList(APIView):
    def get(self, request):
        pedidos_materiales = PedidoMaterial.objects.all()
        serializer = PedidoMaterialSerializer(pedidos_materiales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PedidoMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)