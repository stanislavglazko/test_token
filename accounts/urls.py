from django.urls import path

from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path('all-profiles', UserProfileListCreateView.as_view(),
         name='all-profiles'),
    path('profile/<int:pk>', UserProfileDetailView.as_view(),
         name='profile'),
]
