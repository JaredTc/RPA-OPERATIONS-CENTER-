
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('op_rpas/', include('op_rpas.urls')),

    # --- ENDPOINTS DE SWAGGER / OPENAPI ---
    # Genera el archivo schema.yml / JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Interfaz gráfica de Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Interfaz alternativa de Redoc
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
