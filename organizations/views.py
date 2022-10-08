from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from helpers.renderers import Renderer
from organizations.models import Organization, GroupHead, OrganizationLocation, OrganizationDepartment, OrganizationPosition, StaffClassification
from .serializers import ViewGroupHeadSerializers, ViewOrganizationSerializers, CreateOrganizationSerializers, UpdateOrganizationSerializers, DeactivateOrganizationSerializers, CreateGroupHeadSerializers, UpdateGroupHeadSerializers, DeactivateGroupHeadSerializers, CreateOrganizationLocationSerializers, UpdateOrganizationLocationSerializers, ViewOrganizationLocationSerializers, DeactivateOrganizationLocationSerializers, ViewOrganizationDepartmentSerializers, UpdateOrganizationDepartmentSerializers, CreateOrganizationDepartmentSerializers, DeactivateOrganizationDepartmentSerializers, ViewOrganizationPositionSerializers, UpdateOrganizationPositionSerializers, CreateOrganizationPositionSerializers, DeactivateOrganizationPositionSerializers, ViewStaffClassificationSerializers, UpdateStaffClassificationSerializers, CreateStaffClassificationSerializers, DeactivateStaffClassificationSerializers
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.



# get specific organization
# class ViewOrganization(APIView):
#     permission_classes = [IsAuthenticated]
#     renderer_classes = [Renderer]
#     # def get_object(self, pk):
#     #     try:
#     #         return Organization.objects.get(pk=pk)
#     #     except:
#     #         return Response("pk doesn't exist")


#     def get(self, request, pk):
#         try:
#             organization_object = self.get_object(pk)
#             serialize_object = ViewOrganizationSerializers(organization_object)
#             is_active = serialize_object.data.get('organization_is_active')
#             if is_active==False:
#                 return Response({'status':202, 'msg': 'Please activate the organization first'})
#             else:
#                 return Response({'status':200, 'data': serialize_object.data}, status=status.HTTP_200_OK)
#         except:
#             return Response({'status':400, 'errors':{'AttributeError':['ID does not exists']}}, status=status.HTTP_400_BAD_REQUEST)


# # shows all organization




# class ViewAllOrganizations(APIView): 
#     def get(self, request):
#         try:
#             get_organization = Organization.objects.all()
#             serializer = ViewOrganizationSerializers(get_organization, many=True)
#             return Response({'status':200,'data':serializer.data})
#         except:
#             return Response({'status':404, "errors": serializer.errors})


# #show all deactivate organizations
# class ViewDeactivateOrganization(APIView):
#     def get(self, request):
#         try:
#             val = self.kwargs['val'] 
#             # get_organization = Organization.objects.filter(organization_is_active=False)
#             # serializer = ViewOrganizationSerializers(get_organization, many=True)
#             if val=='all':
#                 get_organization = Organization.objects.filter(organization_is_active=False)
#                 serializer = ViewOrganizationSerializers(get_organization, many=True)
#                 return Response({'status':200,'data':serializer.data})
#         except:
#             return Response({'status':404, "errors": serializer.errors})

# #show all active organization    
# class ViewActivateOrganization(APIView):
#     def get(self, request):
#         try:
#             get_organization = Organization.objects.filter(organization_is_active=True)
#             serializer = ViewOrganizationSerializers(get_organization, many=True)
#             return Response({'status':200,'data':serializer.data})
#         except:
#             return Response({'status':404, "errors": serializer.errors})



# class CreateOrganization(APIView): 
#     # permission_classes = [IsAuthenticated]
#     renderer_classes = [Renderer]
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request):
#         serializer = CreateOrganizationSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':201, 'data':serializer.data, 'msg':'Successfully added'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'status':400, 'data': serializer.errors, 'msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class UpdateOrganization(APIView): 
#     permission_classes = [IsAuthenticated]
#     renderer_classes = [Renderer]
#     def get_object(self, pk):
#         try:
#             return Organization.objects.get(pk=pk)
#         except:
#             return Response("pk doesn't exist")

#     def get(self, request, pk):
#         organization_object = self.get_object(pk)
#         serialize_object = UpdateOrganizationSerializers(organization_object)
#         return Response(serialize_object.data)

#     def put(self, request, pk):
#         organization_object = self.get_object(pk)
#         serializer = UpdateOrganizationSerializers(organization_object, data = request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# # class DeleteOrganization(APIView):
# #     permission_classes = [IsAuthenticated]
# #     renderer_classes = [Renderer]
# #     def get_object(self, pk):
# #         try:
# #             return organization.objects.get(pk=pk)
# #         except:
# #             return Response("pk doesn't exist")
    
# #     def delete(self, request, pk):
# #         try:
# #             obj = self.get_object(pk)
# #             obj.delete()
# #             return Response(status=status.HTTP_204_NO_CONTENT)
# #         except:
# #             return Response({'status':400 ,'msg': 'Organization doesnot get deleted successfully'}, status=status.HTTP_400_BAD_REQUEST)

# # Deactivate organization



# class DeactivateOrganization(APIView):
#     permission_classes = [IsAuthenticated]
#     renderer_classes = [Renderer]
#     def get_object(self, pk):
#         try:
#             return Organization.objects.get(pk=pk)
#         except:
#             return Response("pk doesn't exist")
    
#     def post(self, request, pk):
#         try:
#             obj = self.get_object(pk)
#             if obj.organization_is_active == False:
#                 return Response({'status':200, 'msg': 'Organization is already inactivated'})
            
#             obj.organization_is_active = True
#             obj.save()
#             serializer = DeactivateOrganizationSerializers(obj)
#             return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
#         except:
#             return Response({'status':404 ,'msg': 'Organization doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)



    

# Organization Logic
class OrganizationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]

    def list(self, request):
        try:
            obj = Organization.objects.all()
            serializer = ViewOrganizationSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors": serializer.errors})

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            obj = Organization.objects.get(id=id)
            if obj.organization_is_active == False:
                msg = "Please update the organization status to active"
                return Response({'status':200, 'msg':msg})
            serializer = ViewOrganizationSerializers(obj, many=False)
            return Response({'status':200,'data':serializer.data})

    def create(self, request):
        serializer = CreateOrganizationSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data, 'msg':'Successfully added'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':400, 'data': serializer.errors, 'msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        id = pk
        obj = Organization.objects.get(pk=id)    
        serializer = UpdateOrganizationSerializers(obj, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'data': serializer.data, 'msg': 'Updated Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        obj = Organization.objects.get(id=pk)
        if obj.organization_is_active == False:
            msg = "Organization is already deactivated"
            return Response({'status':200, 'msg':msg})
        try:
            obj.organization_is_active = False
            obj.save()
            serializer = DeactivateOrganizationSerializers(obj)
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':404 ,'msg': 'Organization doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)


# Group head logic
class GroupHeadViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]
    
    def list(self, request):
        try:
            obj = GroupHead.objects.all()
            serializer = ViewGroupHeadSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors":  "Not Found"})

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            obj = GroupHead.objects.get(id=id)
            serializer = ViewGroupHeadSerializers(obj, many=False)
            return Response({'status':200,'data':serializer.data})
        else:
            return Response({'status':404,'data':serializer.errors, 'msg': "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CreateGroupHeadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data, 'msg':'Successfully created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':404, 'msg':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
    
    def update(self, request, pk):
        id = pk
        obj = GroupHead.objects.get(pk=id)    
        serializer = UpdateGroupHeadSerializers(obj, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'data': serializer.data, 'msg': 'Updated Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        obj = GroupHead.objects.get(id=pk)
        if obj.is_active == False:
            msg = "Grouphead is already deactivated"
            return Response({'status':200, 'msg':msg})
        try:
            obj.is_active = False
            obj.save()
            serializer = DeactivateGroupHeadSerializers(obj, many=False)
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':404 ,'msg': 'Organization doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)


# Organization Location Logic
class OrganizationLocationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]
    def list(self, request):
        try:
            obj = OrganizationLocation.objects.all()
            serializer = ViewOrganizationLocationSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors":  "Not Found"})

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            obj = OrganizationLocation.objects.get(id=id)
            serializer = ViewOrganizationLocationSerializers(obj, many=False)
            return Response({'status':200,'data':serializer.data})
        else:
            return Response({'status':404,'data':serializer.errors, 'msg': "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CreateOrganizationLocationSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data, 'msg':'Successfully created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':404, 'msg':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
    
    def update(self, request, pk):
        id = pk
        obj = OrganizationLocation.objects.get(pk=id)    
        serializer = UpdateOrganizationLocationSerializers(obj, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'data': serializer.data, 'msg': 'Updated Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        obj = OrganizationLocation.objects.get(id=pk)
        if obj.is_active == False:
            msg = "This location is already deactivated"
            return Response({'status':200, 'msg':msg})
        try:
            obj.is_active = False
            obj.save()
            serializer = DeactivateOrganizationLocationSerializers(obj, many=False)
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':404 ,'msg': 'Location doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)


# organization Department Logic
class OrganizationDepartmentViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]
    def list(self, request):
        try:
            obj = OrganizationDepartment.objects.all()
            serializer = ViewOrganizationDepartmentSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors":  "Not Found"})

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            obj = OrganizationDepartment.objects.get(id=id)
            serializer = ViewOrganizationDepartmentSerializers(obj, many=False)
            return Response({'status':200,'data':serializer.data})
        else:
            return Response({'status':404,'data':serializer.errors, 'msg': "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CreateOrganizationDepartmentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data, 'msg':'Successfully created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':404, 'msg':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
    
    def update(self, request, pk):
        id = pk
        obj = OrganizationDepartment.objects.get(pk=id)    
        serializer = UpdateOrganizationDepartmentSerializers(obj, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'data': serializer.data, 'msg': 'Updated Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        obj = OrganizationDepartment.objects.get(id=pk)
        if obj.is_active == False:
            msg = "This location is deactivated not working"
            return Response({'status':200, 'msg':msg})
        try:
            obj.is_active = False
            obj.save()
            serializer = DeactivateOrganizationDepartmentSerializers(obj, many=False)
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':404 ,'msg': 'Organization doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)

# Organization Position Logic
class OrganizationPositionViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # prenderer_classes = [Renderer]
    def list(self, request):
        try:
            obj = OrganizationPosition.objects.all()
            serializer = ViewOrganizationPositionSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors":  "Not Found"})

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            obj = OrganizationPosition.objects.get(id=id)
            serializer = ViewOrganizationPositionSerializers(obj, many=False)
            return Response({'status':200,'data':serializer.data})
        else:
            return Response({'status':404,'data':serializer.errors, 'msg': "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CreateOrganizationPositionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data, 'msg':'Successfully created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':404, 'msg':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
    
    def update(self, request, pk):
        id = pk
        obj = OrganizationPosition.objects.get(pk=id)    
        serializer = UpdateOrganizationPositionSerializers(obj, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'data': serializer.data, 'msg': 'Updated Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        obj = OrganizationPosition.objects.get(id=pk)
        if obj.is_active == False:
            msg = "This location is deactivated not working"
            return Response({'status':200, 'msg':msg})
        try:
            obj.is_active = False
            obj.save()
            serializer = DeactivateOrganizationPositionSerializers(obj, many=False)
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':404 ,'msg': 'Organization doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)


# staff classification viewset
class StaffClassificationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # prenderer_classes = [Renderer]
    def list(self, request):
        try:
            obj = StaffClassification.objects.all()
            serializer = ViewStaffClassificationSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':404, "errors":  "Not Found"})

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            obj = StaffClassification.objects.get(id=id)
            serializer = ViewStaffClassificationSerializers(obj, many=False)
            return Response({'status':200,'data':serializer.data})
        else:
            return Response({'status':404,'data':serializer.errors, 'msg': "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CreateStaffClassificationSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'data':serializer.data, 'msg':'Successfully created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':404, 'msg':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        
    
    def update(self, request, pk):
        id = pk
        obj = StaffClassification.objects.get(pk=id)    
        serializer = UpdateStaffClassificationSerializers(obj, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'data': serializer.data, 'msg': 'Updated Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        obj = StaffClassification.objects.get(id=pk)
        if obj.is_active == False:
            msg = "This location is deactivated not working"
            return Response({'status':200, 'msg':msg})
        try:
            obj.is_active = False
            obj.save()
            serializer = DeactivateStaffClassificationSerializers(obj, many=False)
            return Response({'status':200, 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':404 ,'msg': 'Organization doesnot exists or get inactivated successfully'}, status=status.HTTP_404_NOT_FOUND)