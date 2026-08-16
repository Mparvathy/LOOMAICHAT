from django.contrib.auth import authenticate
from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import RegisterSerializer



def home(request):
    return render(request, 'home.html')


def register_page(request):
    return render(request, 'register.html')


# def login_page(request):
#     return render(request, 'home.html')  # or a dedicated login.html


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
    
# class LoginAPIView(APIView):
#     """POST username, password -> returns a token."""
#     permission_classes = [permissions.AllowAny]
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(
#             username=serializer.validated_data['username'],
#             password=serializer.validated_data['password'],
#         )
#         if user is None:
#             return Response({'detail': 'Invalid username or password.'}, status=401)

#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'user': UserSerializer(user).data})


# class ProfileAPIView(generics.RetrieveUpdateAPIView):
#     """GET/PATCH the logged-in user. Requires header: Authorization: Token <key>"""
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self):
#         return self.request.user