from rest_framework.routers import DefaultRouter

from .viewsets import UserProfileDetailViewSets

router = DefaultRouter()
router.register('', UserProfileDetailViewSets)
urlpatterns = router.urls
