from rest_framework.routers import DefaultRouter
from .viewsets import UserProfileDetailViewSets, UserDetailViewSets

router = DefaultRouter()
router.register('accounts', UserProfileDetailViewSets)
router.register('users', UserDetailViewSets)
urlpatterns = router.urls
