from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PassHolderViewSet

router_v1 = DefaultRouter()
router_v1.register(r'pass-holders', PassHolderViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
