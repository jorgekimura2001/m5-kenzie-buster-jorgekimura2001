from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .permissions import UserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserViewParams(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UserPermission]

    def get(self, request: Request, user_id=int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
