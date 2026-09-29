# BACKEND RPA OPERATIONS CENTER

# 📂 Estructura del proyecto

```bash
RPA_OPERATIONS/
├── op_rpas/                    # Aplicación principal
│   ├── auth/                   # Submódulo: Autenticación (LoginView, JWT)
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── users/                  # Submódulo: Gestión de Usuarios (UserViewSet)
│   │   ├── serializer.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── templates/              # Plantillas HTML para envíos de correo
│   ├── models.py               # Modelo de usuario personalizado (Custom_User)
│   └── urls.py                 # Enrutador central de la app op_rpas
├── RPA_OPERATIONS/             # Configuración global del proyecto
│   ├── settings.py             # Variables de entorno, BD, CORS, JWT y Email
│   └── urls.py                 # Rutas raíz y endpoints de Swagger UI
├── .env                        # Credenciales y variables de entorno
├── manage.py                   # Script de gestión de Django
└── requirements.txt            # Dependencias del proyecto
```
