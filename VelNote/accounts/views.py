from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import VelNoteUser
from .serializers import VelNoteUserSerializer, UserRoleSerializer
from .serializers import FileUploadSerializer
from .serializers import LoginSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status









class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)

        return Response( {
            'access': str(access_token),
            'refresh': str(refresh_token),
            'email': user.email,
            'username': user.username
        }, status=status.HTTP_200_OK )


class UserCreateView(generics.CreateAPIView):
    queryset = VelNoteUser.objects.all()
    serializer_class = VelNoteUserSerializer
    permission_classes = [permissions.AllowAny]

class UserRoleUpdateView(generics.UpdateAPIView):
    queryset = VelNoteUser.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Update the role of the logged-in user


class FileUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class HOME(APIView):
    permission_classes = [IsAuthenticated]  # authenticated

    def get(self, request):
        username = request.user.username  
        return Response({'username': username}, status=status.HTTP_200_OK)
