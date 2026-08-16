from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema

def home(request):
    return render(request, 'home.html')


def register_page(request):
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')  

def mainscreen(request):
    return render(request, 'mainscreen.html')

# ---------- DRF API ----------
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()          # user is created here

        return Response(
            {"detail": "Account created successfully."},
            status=status.HTTP_201_CREATED
        )

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer          # important for Swagger
    @swagger_auto_schema(
        request_body=LoginSerializer,           # this makes the fields appear
        responses={
            200: 'Token + username returned',
            401: 'Invalid credentials'
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )

        if user is None:
            return Response(
                {'detail': 'Invalid username or password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'username': user.username,
        })
    
# class ProfileAPIView(generics.RetrieveUpdateAPIView):
#     """GET/PATCH the logged-in user. Requires header: Authorization: Token <key>"""
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         return self.request.user
