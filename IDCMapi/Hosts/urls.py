from .views import HostViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hosts', HostViewset, basename='hosts')
urlpatterns = router.urls