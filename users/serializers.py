from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["email", "password", ]
        extra_kwargs = {"password": {"write_only": True}}


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_active', ]
