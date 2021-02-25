from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileDetailViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
