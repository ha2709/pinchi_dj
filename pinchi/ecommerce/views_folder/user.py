from ..models.user import User
from ..serializers.user import UserSerializer
from django.http import JsonResponse
from django.views import View
from asgiref.sync import sync_to_async
 
 
class UserListView(View):
    
    
    async def get(self, request, *args, **kwargs):
        users = await sync_to_async(list)(User.objects.all())
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
