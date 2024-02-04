# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from ecommerce.models.shopping_cart import ShoppingCart
from ecommerce.serializers.product import ProductSerializer

@api_view(['GET'])
def view_cart(request):
    # Retrieve the cart from the session or create a new one
    cart, created = ShoppingCart.objects.get_or_create(pk=request.session.get('cart_id'))
    
    serializer = ProductSerializer(cart.products.all(), many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request, product_id):
    # Retrieve the cart from the session or create a new one
    cart, created = ShoppingCart.objects.get_or_create(pk=request.session.get('cart_id'))
    
    try:
        product = Product.objects.get(pk=product_id)
        cart.products.add(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def remove_from_cart(request, product_id):
    # Retrieve the cart from the session or create a new one
    cart, created = ShoppingCart.objects.get_or_create(pk=request.session.get('cart_id'))
    
    try:
        product = Product.objects.get(pk=product_id)
        cart.products.remove(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
