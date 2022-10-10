from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import HrmsUserLoginSerializer, HrmsUserProfileSerializer, HrmsUserChangePasswordSerializer, SendPasswordResetEmailSerializer, HrmsUserPasswordResetSerializer, HrmsUserLogoutSerializer
from django.contrib.auth import authenticate
from helpers.renderers import Renderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refreshToken': str(refresh),
        'accessToken': str(refresh.access_token),
    }


class HrmsUserLogin(APIView):
    renderer_classes = [Renderer]
    def post(self, request, format=None):
        serializer = HrmsUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                uid = user.id
                uemail = user.email
                token = get_tokens_for_user(user)
                return Response({'status': 200, 'token': token, 'uid':uid, 'msg':'Login Successful'}, status=status.HTTP_200_OK)
            else: 
                return Response({'status': 404, 'errors':{'non_field_errors':['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'status': 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class HrmsUserProfile(APIView):
    renderer_classes = [Renderer]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            serializer = HrmsUserProfileSerializer(request.user)
            
            return Response({'status':200,'data':serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 400, 'msg': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


class HrmsUserChangePassword(APIView):
    renderer_classes = [Renderer]
    def post(self, request):
        serializer = HrmsUserChangePasswordSerializer(data=request.data, context={'hrms_user':request.user})
        if serializer.is_valid():
            return Response({'status': 200, 'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)            

class SendPasswordResetEmail(APIView):
    renderer_classes = [Renderer]
    def post(self, request):
        serializer = SendPasswordResetEmailSerializer(data = request.data)
        if serializer.is_valid():
            return Response({'msg': 'Password Reset link send. Please check your email'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class HrmsUserResetPassword(APIView):
    renderer_classes = [Renderer]
    def post(self, request, uid, token):
        serializer = HrmsUserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        if serializer.is_valid():
            return Response({'status': 200, 'msg': 'password is reset successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class HrmsUserLogout(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    
    def post(self, request, format=None):
        serializer = HrmsUserLogoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 204}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'status': 400, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    


