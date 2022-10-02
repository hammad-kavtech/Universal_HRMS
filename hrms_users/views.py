from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import HrmsUserLoginSerializer, HrmsUserProfileSerializer, HrmsUserChangePasswordSerializer, SendPasswordResetEmailSerializer, HrmsUserPasswordResetSerializer
from django.contrib.auth import authenticate
from .models import HrmsUsers
from .renderers import HrmsUserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class HrmsUserLogin(generics.UpdateAPIView):
    # renderer_classes = [HrmsUserRenderer]

    def post(self, request, format=None):
        serializer = HrmsUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token ,'msg':'Login Successful'}, status=status.HTTP_200_OK)
        else: 
            return Response({'errors':{'non_field_errors':['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
    

class HrmsUserProfile(APIView):
    # renderer_classes = [HrmsUserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = HrmsUserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HrmsUserChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = HrmsUserChangePasswordSerializer(data=request.data, context={'hrms_user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmail(APIView):
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset link send. Please check your email'}, status=status.HTTP_200_OK)


class HrmsUserResetPassword(APIView):
    def post(self, request, uid, token, format=None):
        serializer = HrmsUserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
        


        

