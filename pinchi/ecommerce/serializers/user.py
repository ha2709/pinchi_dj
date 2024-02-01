from rest_framework import serializers
from ..models.user import User
# from django.contrib.auth import get_user_model
# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    customer_category = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'customer_category']

    def get_customer_category(self, obj):
        return obj.get_customer_category()
