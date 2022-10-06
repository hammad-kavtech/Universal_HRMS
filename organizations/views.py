from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from helpers.renderers import Renderer
from organizations.models import Organization
from .serializers import ViewOrganizationSerializers, CreateOrganizationSerializers, UpdateOrganizationSerializers, DeactivateOrganizationSerializers, CreateGroupHeadSerializers
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


# get specific organization
class ViewOrganization(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except:
            return Response("pk doesn't exist")


    def get(self, request, pk):
        try:
            organization_object = self.get_object(pk)
            serialize_object = ViewOrganizationSerializers(organization_object)
            is_active = serialize_object.data.get('organization_is_active')
            if is_active==False:
                return Response({'status':202, 'msg': 'Please activate the organization first'})
            else:
                return Response({'status':200, 'data': serialize_object.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':400, 'errors':{'AttributeError':['ID does not exists']}}, status=status.HTTP_400_BAD_REQUEST)


# shows all organization




class ViewAllOrganizations(APIView): 
    def get(self, request):
        try:
            get_organization = Organization.objects.all()
            serializer = ViewOrganizationSerializers(get_organization, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors": serializer.errors})


#show all deactivate organizations
class ViewDeactivateOrganization(APIView):
    def get(self, request):
        try:
            val = self.kwargs['val'] 
            # get_organization = Organization.objects.filter(organization_is_active=False)
            # serializer = ViewOrganizationSerializers(get_organization, many=True)
            if val=='all':
                get_organization = Organization.objects.filter(organization_is_active=False)
                serializer = ViewOrganizationSerializers(get_organization, many=True)
                return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors": serializer.errors})

#show all active organization    
class ViewActivateOrganization(APIView):
    def get(self, request):
        try:
            get_organization = Organization.objects.filter(organization_is_active=True)
            serializer = ViewOrganizationSerializers(get_organization, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors": serializer.errors})



class CreateOrganization(APIView): 
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = CreateOrganizationSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':400, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrganization(APIView): 
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except:
            return Response("pk doesn't exist")

    def get(self, request, pk):
        organization_object = self.get_object(pk)
        serialize_object = UpdateOrganizationSerializers(organization_object)
        return Response(serialize_object.data)

    def put(self, request, pk):
        organization_object = self.get_object(pk)
        serializer = UpdateOrganizationSerializers(organization_object, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class DeleteOrganization(APIView):
#     permission_classes = [IsAuthenticated]
#     renderer_classes = [Renderer]
#     def get_object(self, pk):
#         try:
#             return organization.objects.get(pk=pk)
#         except:
#             return Response("pk doesn't exist")
    
#     def delete(self, request, pk):
#         try:
#             obj = self.get_object(pk)
#             obj.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except:
#             return Response({'status':400 ,'msg': 'Organization doesnot get deleted successfully'}, status=status.HTTP_400_BAD_REQUEST)

# Deactivate organization
class DeactivateOrganization(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]
    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except:
            return Response("pk doesn't exist")
    
    def post(self, request, pk):
        try:
            obj = self.get_object(pk)
            if obj.organization_is_active == False:
                return Response({'status':200, 'msg': 'Organization is already inactivated'})
            
            obj.organization_is_active = True
            obj.save()
            serializer = DeactivateOrganizationSerializers(obj)
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':404 ,'msg': 'Organization doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)


# class CreateGroupHead():

class CreateGroupHead(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [Renderer]

    def post(self, request):
        serializer = CreateGroupHeadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':400, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

