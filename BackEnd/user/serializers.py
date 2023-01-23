from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from user.models import AdminAccount, User, UserType, IDType


class AdminAccountCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = AdminAccount
        fields = (
            "id",
            "admin_name",
            "email",
        )

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'
        
class IDTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDType
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
