from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # input validation
        if not request.data.get('username') or not request.data.get('password'):
            return Response({'detail': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        

        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))

        if user:
            refresh = RefreshToken.for_user(user)   
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:

            user = serializer.save()
            
            return Response({
                'detail': 'Account Successfully created',
                'user_id': user.id,
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        # if CustomUser.objects.filter(username=username).exists():
        #     return Response(
        #         {"detail": "Username already exists"},
        #         status=status.HTTP_400_BAD_REQUEST)
        
        # user = CustomUser.objects.create_user(
        #     username = username,
            
        # )
        # user.set_password(password)
        # user.save()
        # return Response({"detail": "User created successfully"}, status=status.HTTP_201_CREATED)
    
        