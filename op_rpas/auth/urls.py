from django.urls import path, include

from op_rpas.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]