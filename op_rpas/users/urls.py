from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from op_rpas.users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]