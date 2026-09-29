# 🚀 BACKEND RPA OPERATIONS CENTER

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2_LTS-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14+-red?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![JWT](https://img.shields.io/badge/JWT-SimpleJWT-black?logo=jsonwebtokens&logoColor=white)](https://django-rest-framework-simplejwt.readthedocs.io/)
[![Swagger](https://img.shields.io/badge/OpenAPI-Swagger_UI-85EA2D?logo=swagger&logoColor=black)](https://drf-spectacular.readthedocs.io/)

Backend robusto y escalable desarrollado en Python con **Django REST Framework** y **MySQL** para la administración centralizada de operaciones RPA, gestión de usuarios y autenticación segura mediante tokens JWT. Utiliza variables de entorno (`.env`) para la gestión segura de credenciales y conexión a base de datos remota en servidor propio.

---

## 🛠️ Tecnologías y Librerías Utilizadas

* **Framework:** Django 4.2 LTS / Django REST Framework
* **Base de Datos:** MySQL (Servidor remoto propio)
* **Autenticación:** SimpleJWT (`rest_framework_simplejwt`)
* **Documentación:** OpenAPI 3 / Swagger UI (`drf-spectacular`)
* **Notificaciones:** SMTP Email Engine con renderizado de plantillas HTML
* **Entorno:** `django-environ` para gestión segura de variables de entorno

---

## ⚙️ Características Implementadas

* **Autenticación Segura (JWT):**
  * Inicio de sesión de usuarios con generación de tokens `access` y `refresh`.
  * Middleware de permisos dinámicos (`AllowAny` para login/registro, `IsAuthenticated` para endpoints privados).
* **Gestión Centralizada de Usuarios (`UserViewSet`):**
  * CRUD unificado basado en `ModelViewSet` para consumo eficiente de la API.
  * Registro público de usuarios con encriptado automático de contraseña mediante `create_user`.
  * Paginación global integrada y ordenamiento cronológico por fecha de registro (`-date_joined`).
* **Servicio de Notificaciones por Correo:**
  * Disparo automático de correos HTML de bienvenida tras el registro mediante `perform_create`.
* **Documentación Interactiva (Swagger UI):**
  * Mapeo de esquema OpenAPI 3 con soporte interactivo para probar tokens JWT (`BearerAuth`).

---

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura **Modular basada en Características (Feature-Based Modular Structure)**, desacoplando cada submódulo con sus propios controladores, serializadores y rutas:

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
│   ├── templates/              # Plantillas HTML locales para envíos de correo
│   │   └── emails/
│   │       └── email-templated.html
│   ├── models.py               # Modelo de usuario personalizado (Custom_User)
│   └── urls.py                 # Enrutador central de la app op_rpas
├── RPA_OPERATIONS/             # Configuración global del proyecto
│   ├── settings.py             # Variables de entorno, BD, CORS, JWT y Email
│   └── urls.py                 # Rutas raíz y endpoints de Swagger UI
├── templates/                  # Plantillas globales
├── .env                        # Credenciales y variables de entorno (Ignorado en Git)
├── manage.py                   # Script de gestión de Django
└── requirements.txt            # Dependencias del proyecto
