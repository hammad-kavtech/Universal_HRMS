from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from helpers.renderers import Renderer
from organizations.models import organization
from hrms_users.models import HrmsUsers
from hrms_users.views import HrmsUserProfile
from .serializers import ViewOrganizationSerializers, CreateOrganizationSerializers, UpdateOrganizationSerializers, DeleteOrganizationSerializers
# Create your views here.


    
# def get_hrms_user_status():
#     getData = HrmsUserProfile 
#     return getData


class ViewOrganization(APIView):
    # is_active = get_hrms_user_status()
    # if is_active == False:
    #     Response('User is inactive. Please active first') 

    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    def get_object(self, pk):
        try:
            return organization.objects.get(pk=pk)
        except:
            return Response("pk doesn't exist")


    def get(self, request, pk):
        try:
            organization_object = self.get_object(pk)
            serialize_object = ViewOrganizationSerializers(organization_object)
            return Response(serialize_object.data)
        except:
            return Response({'status':400, 'errors':{'AttributeError':['ID does not exists']}}, status=status.HTTP_400_BAD_REQUEST)

#class ViewAllOrganizations(APIView)
    # def get(self, request):
    #     get_organization = organization.objects.all()
    #     serializer = ViewOrganizationSerializers(get_organization, many=True)
    #     return Response(serializer.data)

class CreateOrganization(APIView): 
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    def post(self, request):
        serializer = CreateOrganizationSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201}, serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':400}, serializer.errors, status=status.HTTP_400_CREATED)


class UpdateOrganization(APIView): 
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    def get_object(self, pk):
        try:
            return organization.objects.get(pk=pk)
        except:
            return Response("pk doesn't exist")

    def get(self, request, pk):
        organization_object = self.get_object(pk)
        serialize_object = UpdateOrganizationSerializers(organization_object)
        return Response(serialize_object.data)

    def put(self, request, pk):
        organization_object = self.get_object(pk)
        serializer = UpdateOrganizationSerializers(organization_object, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200}, serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'status':400}, serializer.errors, status=status.HTTP_400_CREATED)

class DeleteOrganization(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    def get_object(self, pk):
        try:
            return organization.objects.get(pk=pk)
        except:
            return Response("pk doesn't exist")
    
    def delete(self, request, pk):
        try:
            obj = self.get_object(pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'status':400 ,'msg': 'Organization doesnot get deleted successfully'}, status=status.HTTP_400_BAD_REQUEST)