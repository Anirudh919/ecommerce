from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomTokenObtainPairSerializer
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
        description="API documentation for E-Commerce backend",
    ),
    public=True,
)

router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer)),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls