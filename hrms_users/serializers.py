from xml.dom import ValidationErr
from django.forms import ValidationError
from rest_framework import serializers
from .models import HrmsUsers
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util

class HrmsUserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model = HrmsUsers
        fields = ['email', 'password']

class HrmsUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HrmsUsers
        fields = ['id', 'email']


class HrmsUserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, 
        style={'input-type':'password'}, 
        write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, 
        style={'input-type':'password'}, 
        write_only=True
    )
    class Meta:
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('hrms_user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs 


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if HrmsUsers.objects.filter(email=email).exists():
            user = HrmsUsers.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token+'/'
            print('Password Reset Link', link)
            
            #send email
            body = 'Click the Following link to  Reset your Password ' + link
            data = {
                'subject': 'Reset your Password',
                'body':  body,
                'to_email': user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationErr('You are not a registered User')


class HrmsUserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, 
        style={'input-type':'password'}, 
        write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, 
        style={'input-type':'password'}, 
        write_only=True
    )
    class Meta:
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        try:     
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = HrmsUsers.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationError('Token is not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError:
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationError('Token is not valid or Expired')
