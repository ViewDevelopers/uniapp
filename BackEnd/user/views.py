from rest_framework import viewsets
from rest_framework import permissions
from user.models import User, AdminAccount, UserType, IDType
from .serializers import (
    UserSerializer,
    AdminAccountCreateSerializer,
    IDTypeSerializer,
    UserTypeSerializer,
)


class AdminAccountViewSet(viewsets.ModelViewSet):
    queryset = AdminAccount.objects.all()
    serializer_class = AdminAccountCreateSerializer
    permission_classes = [permissions.AllowAny]


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
    permission_classes = [permissions.AllowAny]


class IDTypeViewSet(viewsets.ModelViewSet):
    queryset = IDType.objects.all()
    serializer_class = IDTypeSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# api con Apiview, descomente para utilizar

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from user.models import User, AdminAccount


# class ListUsersView(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def get(self, request, format=None):
#         if User.objects.all().exists():
#             users = User.objects.all()

#             result = []

#             for user in users:
#                 item = {}
#                 item["admin"] = user.id_admin.admin_name
#                 item["type_identification"] = user.id_type_identification.name_id_type
#                 item["type_user"] = user.id_type_user.name_user_type
#                 item["identification"] = user.identification_number
#                 item["full_name"] = user.get_full_name()
#                 item["email"] = user.email
#                 item["telephone"] = user.telephone
#                 result.append(item)
#             return Response({"users": result}, status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {"error": "No users found"},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
