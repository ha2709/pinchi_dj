from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.registration import UserRegistrationSerializer
from ..utils.send_email import send_verification_email
User = get_user_model()

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()

            token = RefreshToken.for_user(user).access_token
            verification_url = reverse('email-verify')
            absolute_url = f"{request.build_absolute_uri(verification_url)}?token={str(token)}"
           
            # Use custom function to send verification email
            send_verification_email(user.email, absolute_url)
            # Including the verification link in the response
            response_data = serializer.data
            response_data['verification_link'] = absolute_url

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
