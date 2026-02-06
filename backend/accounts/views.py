from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer

from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny


# ======================
# REGISTER API
# ======================
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ======================
# LOGIN API (NO JWT)
# ======================
class LoginAPIView(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]

    def post(self, request):
        print("RAW BODY:", request.body)
        print("PARSED DATA:", request.data)

        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"error": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=400)

        user = authenticate(username=user_obj.username, password=password)

        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        return Response({
            "message": "Login successful",
            "username": user.username,
            "email": user.email,
        })

