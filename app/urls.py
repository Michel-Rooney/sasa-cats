from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('api/cat', views.CatViewSets, basename='api-cat')

urlpatterns = router.urls
