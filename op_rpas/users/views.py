from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from op_rpas.models import Custom_User
from op_rpas.users.serializer import (
    UserRegistrationSerializer,
    UpdateUserSerializer,
    UserSerializer
)


def email_welcome(email_destino):
    try:
        subject = '¡Bienvenido a nuestro sitio!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email_destino]

        template = get_template('emails/email-templated.html')
        content = template.render({})

        email = EmailMessage(subject, content, from_email, recipient_list)
        email.content_subtype = "html"
        email.send(fail_silently=False)
        print(f"--> Correo enviado exitosamente a {email_destino}")
    except Exception as e:
        print(f"--> ERROR enviando correo: {str(e)}")


class UserViewSet(viewsets.ModelViewSet):
    queryset = Custom_User.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateUserSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = serializer.save()
        if user.email:
            email_welcome(user.email)