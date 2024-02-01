# utils.py
from ecommerce.models.discount import Discount

def apply_discount_to_order(user, total_price):
    user_category = user.get_customer_category()
    discounts = Discount.objects.filter(user_category=user_category)

    for discount in discounts:
        total_price -= (total_price * (discount.percentage / 100))

    return total_price
