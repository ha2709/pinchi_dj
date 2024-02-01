# myapp/urls.py

from django.urls import path
from .views_folder.user import UserListView  # Import your view here
from .views_folder.registration import UserRegistrationView
from .views_folder.verification import VerifyEmail

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),

]
