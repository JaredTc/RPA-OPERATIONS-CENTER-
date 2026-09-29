


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from op_rpas.users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
    # Tus otras rutas aquí...
    path('auth/', include('op_rpas.auth.urls')),
    path('', include('op_rpas.users.urls')),
]