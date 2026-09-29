from rest_framework import serializers
from op_rpas.models import Custom_User


class UserRegistrationSerializer(serializers.ModelSerializer):
    imgProfile = serializers.URLField(required=False)
    class Meta:
        model = Custom_User
        fields = [
            'first_name',
            'last_name',
            'is_superuser',
            'username',
            'password',
            'email',
            'is_staff',
            'is_active',
            'imgProfile'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        img_profile = validated_data.pop('imgProfile', None)
        user = Custom_User.objects.create_user(**validated_data)

        if img_profile:
            user.imgProfile = img_profile
            user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = [
            'id',
            'first_name',
            'last_name',
            'is_superuser',
            'username',
            'email',
            'is_staff',
            'is_active',
            'imgProfile',
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'imgProfile',
            'is_staff',
            'is_active',
            'is_superuser',
        ]
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'username': {'required': False},
            'email': {'required': False},
            'is_staff': {'required': False},
            'is_active': {'required': False},
            'is_superuser': {'required': False},
            'imgProfile': {'required': False},
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
    # class Meta:
    #     model = CustomUser
    #     fields = [
    #         'first_name',
    #         'last_name',
    #         'username',
    #         'password',
    #         'email',
    #         'position',
    #         'imgProfile',
    #     ]
    #
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.position = validated_data.get('position', instance.position)
    #     instance.imgProfile = validated_data.get('imgProfile', instance.imgProfile)
    #     instance.save()
    #     return instance
