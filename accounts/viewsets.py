from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer


class UserProfileDetailViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserDetailViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
