from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models.product import Product
from ..serializers.product import ProductSerializer
from ..utils.permissions import IsDepartmentStaff

class ProductListCreateAPIView(APIView):
    # Ensure the user is authenticated and is staff of the department
    permission_classes = [IsAuthenticated, IsDepartmentStaff]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            products = Product.objects.filter(category__department=request.user.department)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # You may want to add additional checks here to ensure the user can add products to the specified category/department
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDepartmentStaff]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        if product is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        if product is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        if product is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
