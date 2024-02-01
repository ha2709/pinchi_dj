# views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ecommerce.models.order import Order 
from ecommerce.models.shopping_cart import ShoppingCart 

from ecommerce.serializers.order import OrderSerializer
from ecommerce.utils.discount import apply_discount_to_order

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Retrieve the user's shopping cart
        shopping_cart, _ = ShoppingCart.objects.get_or_create(user=self.request.user)

        # Calculate the total price based on the shopping cart contents
        total_price = sum(product.price for product in shopping_cart.products.all())

        # Apply discounts if any
        total_price = apply_discount_to_order(self.request.user, total_price)

        # Create the order
        serializer.save(user=self.request.user, products=shopping_cart.products.all(), total_price=total_price)

        # Clear the user's shopping cart after placing the order
        shopping_cart.products.clear()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

