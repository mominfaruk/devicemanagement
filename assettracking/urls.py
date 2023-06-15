from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, CheckoutViewSet, ConditionLogViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='device')
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'checkouts', CheckoutViewSet)
router.register(r'condition-logs', ConditionLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # Other URLs
]
