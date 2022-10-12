from asyncio.windows_events import NULL
from django.forms import IntegerField
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from helpers.renderers import Renderer
from organizations.models import Organization, GroupHead, OrganizationLocation, OrganizationDepartment, OrganizationPosition, StaffClassification
from .serializers import GroupHeadSerializers, OrganizationAndLocationSerializers, OrganizationSerializers, OrganizationLocationSerializers, OrganizationDepartmentSerializers, OrganizationPositionSerializers, StaffClassificationSerializers, OrganizationAndLocationSerializers
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



# def getApiArr(self, code, message=''):
#     data = {'status': code, 'message': message}
#     return data

def successMsg():
    return ({'status': 200, 'data': '', 'message': 'Successfully get the response', 'system_error_message': '' })
    
    

# Organization Logic
# class OrganizationViewset(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     renderer_classes = [Renderer]

#     def list(self, request):
#         api_response = successMsg()
#         try:
#             obj = Organization.objects.all()
#             serializer = OrganizationSerializers(obj, many=True)
#             return Response({'status': 200, 'data': serializer.data, 'message':'Success'})
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)

#     def retrieve(self, request, pk=None):
#         api_response = successMsg()
#         try:
#             id=pk
#             if Organization.objects.filter(pk=id).exists():
#                 obj = Organization.objects.get(id=id)
#                 if obj.organization_is_active == False:
#                     msg = "Please update the organization status to active"
#                     return Response({'status':400, 'message': msg})
#                 serializer = OrganizationSerializers(obj, many=False)
#                 return Response({'status':200, 'data':serializer.data, 'message':'Successfully added'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'status':404, 'message': "Organization does not exist in db"}, status=status.HTTP_404_NOT_FOUND)
#         except ValueError:
#             return Response({'status': 404, 'message': 'Dynamic id entered into url is not of type int' })
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)
            


#     def create(self, request):
#         api_response = successMsg()
#         try:
#             serializer = OrganizationSerializers(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'status':201, 'data':serializer.data, 'message':'Successfully added'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'status':400, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)

#     def update(self, request, pk):
#         api_response = successMsg()
#         try:
#             id = pk
#             if Organization.objects.filter(pk=id).exists():
#                 obj = Organization.objects.get(pk=id)  
#                 serializer = OrganizationSerializers(obj, data = request.data, partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
#                 else:
#                     return Response({'status':400, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response({'status':404, 'message': 'This Organization does not exists'})
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)

#     def destroy(self, request, pk):
#         api_response = successMsg()
#         try:
#             id = pk
#             if Organization.objects.filter(pk=id).exists():
#                 obj = Organization.objects.get(id=pk)
#                 if obj.organization_is_active == False:
#                     msg = "Organization is already deactivated"
#                     return Response({'status':200, 'message':msg})
#                 obj.organization_is_active = False
#                 obj.save()
#                 serializer = OrganizationSerializers(obj)
#                 return Response({'status':200, 'data': serializer.data, 'message': 'Deleted Successfully'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'status':404, 'message': 'This Organization does not exists'})
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)

# Organization Location Logic
# class OrganizationLocationViewset(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     # renderer_classes = [Renderer]
#     def list(self, request):
#         api_response = successMsg()
#         try:
#             obj = OrganizationLocation.objects.all()
#             serializer = OrganizationLocationSerializers(obj, many=True)
#             return Response({'status':200,'data':serializer.data, 'message': 'Success'})
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)
 

#     def retrieve(self, request, pk=None):
#         api_response = successMsg()
#         try:
#             id=pk
#             if OrganizationLocation.objects.filter(pk=id).exists():
#                 obj = OrganizationLocation.objects.get(id=id)
#                 serializer = OrganizationLocationSerializers(obj, many=False)
#                 return Response({'status':200,'data':serializer.data, 'message': 'Success'})
#             else:
#                 return Response({'status':404, 'message': 'id does not exists in db'})
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)

#     def create(self, request):
#         api_response = successMsg()
#         try:
#             serializer = OrganizationLocationSerializers(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)
    
#     def update(self, request, pk):
#         api_response = successMsg()
#         try:
#             id = pk
#             if OrganizationLocation.objects.filter(pk=id).exists():
#                 obj = OrganizationLocation.objects.get(pk=id)    
#                 serializer = OrganizationLocationSerializers(obj, data = request.data, partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
#                 else:
#                     return Response({'status':400, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response({'status':404, 'message': 'This id does not exists in db'})
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)

#     def destroy(self, request, pk):
#         api_response = successMsg()
#         try:
#             id = pk
#             if OrganizationLocation.objects.filter(pk=id).exists():
#                 obj = OrganizationLocation.objects.get(id=pk)
#                 if obj.is_active == False:
#                     msg = "This location is already deactivated"
#                     return Response({'status':400, 'message':msg})
#                 obj.is_active = False
#                 obj.save()
#                 serializer = OrganizationLocationSerializers(obj, many=False)
#                 return Response({'status':200, 'data': serializer.data, 'message': 'Successfully Deleted'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'status':404, 'message': "This id does not exist in db"})
#         except Exception as e:
#             api_response['status'] = status.HTTP_400_BAD_REQUEST
#             api_response['system_error_message'] = str(e)
#             api_response['message'] = ''
#             return Response(api_response)


# Group head logic
class GroupHeadViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]

    def list(self, request):
        api_response = successMsg()
        try:    
            obj = GroupHead.objects.all()
            serializer = GroupHeadSerializers(obj, many=True)
            return Response({'status':200, 'data':serializer.data, 'message': 'Success'})
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)


    def retrieve(self, request, pk=None):
        api_response = successMsg()
        try:
            id=pk
            if GroupHead.objects.filter(pk=id).exists():
                obj = GroupHead.objects.get(id=id)
                serializer = GroupHeadSerializers(obj, many=False)
                return Response({'status':200,'data':serializer.data, 'message': 'Success'})
            else:
                return Response({'status':404, 'message': 'This Grouphead does not exists in database'})   
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
     

    def create(self, request):
        api_response = successMsg()
        try:
            serializer = GroupHeadSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
        
    
    def update(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
            
            if GroupHead.objects.filter(pk=id).exists():
                obj = GroupHead.objects.get(pk=id)    
                serializer = GroupHeadSerializers(obj, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status':400, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':404, 'message': 'Grouphead with this index does not exist in db'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)

    def destroy(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
            if GroupHead.objects.filter(pk=id).exists():
                obj = GroupHead.objects.get(id=id)
                if obj.is_active == False:
                    msg = "GroupHead is already deactivated"
                    return Response({'status':200, 'message':msg})
                obj.is_active = False
                obj.save()
                serializer = GroupHeadSerializers(obj)
                return Response({'status':200, 'data': serializer.data, 'message': 'Successfully Deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': 'This Organization does not exists'})
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)



# organization Department Logic
class OrganizationDepartmentViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]
    def list(self, request):
        api_response = successMsg()
        try:
            obj = OrganizationDepartment.objects.all()
            serializer = OrganizationDepartmentSerializers(obj, many=True)
            return Response({'status':200, 'data':serializer.data, 'message': 'Success'})
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
    

    def retrieve(self, request, pk=None):
        api_response = successMsg()
        try:
            id=pk    
            if OrganizationDepartment.objects.filter(pk=id).exists():
                obj = OrganizationDepartment.objects.get(id=id)
                serializer = OrganizationDepartmentSerializers(obj, many=False)
                return Response({'status':200, 'data':serializer.data, 'message': 'Success'})
            else:
                return Response({'status':404, 'message': "Department does not exist at this index"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)

    def create(self, request):
        api_response = successMsg()
        try:
            serializer = OrganizationDepartmentSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
        
    
    def update(self, request, pk):
        api_response = successMsg()
        try:
            id = pk

            if OrganizationDepartment.objects.filter(pk=id).exists():    
                obj = OrganizationDepartment.objects.get(pk=id)    
                serializer = OrganizationDepartmentSerializers(obj, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':404, 'message': "Department does not exist at this index"}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)


    def destroy(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
            obj = OrganizationDepartment.objects.get(id=pk)
            if obj.is_active == False:
                msg = "This Department is already deactivated"
                return Response({'status':200, 'message':msg})
        
            if OrganizationDepartment.objects.filter(pk=id).exists():    
                obj.is_active = False
                obj.save()
                serializer = OrganizationDepartmentSerializers(obj, many=False)
                return Response({'status':200, 'data': serializer.data, 'message': 'Deleted Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': "Department does not exist at this index"}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
            

# Organization Position Logic
class OrganizationPositionViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # prenderer_classes = [Renderer]
    def list(self, request): 
        api_response = successMsg() 
        try:
            obj = OrganizationPosition.objects.all()
            serializer = OrganizationPositionSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data, 'message': 'Success'})
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)


    def retrieve(self, request, pk=None):
        api_response = successMsg()
        try:
            id=pk        
            if OrganizationPosition.objects.filter(pk=id).exists():  
                obj = OrganizationPosition.objects.get(id=id)
                serializer = OrganizationPositionSerializers(obj, many=False)
                return Response({'status':200,'data':serializer.data, 'message': 'Success'})
            else:
                return Response({'status':404, 'message': "Position does not exist at this index"}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)


    def create(self, request):
        api_response = successMsg()
        try:
            serializer = OrganizationPositionSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
        
    
    def update(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
            if OrganizationPosition.objects.filter(pk=id).exists():
                obj = OrganizationPosition.objects.get(pk=id)    
                serializer = OrganizationPositionSerializers(obj, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status':400, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':404, 'message': "Position does not exist at this index"}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)


    def destroy(self, request, pk):
        api_response = successMsg()
        
        try:
            id = pk
            if OrganizationPosition.objects.filter(pk=id).exists(): 
                obj = OrganizationPosition.objects.get(pk=id)
                if obj.is_active == False:
                    msg = "This Position is already deactivated"
                    return Response({'status':404, 'message':msg})
        
                obj.is_active = False
                obj.save()
                serializer = OrganizationPositionSerializers(obj, many=False)
                return Response({'status':200, 'data': serializer.data, 'message': 'Successfully Deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': "Position does not exist at this index"}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)


# staff classification viewset
class StaffClassificationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # prenderer_classes = [Renderer]
    def list(self, request):   
        api_response = successMsg()
        try:
            obj = StaffClassification.objects.all()
            serializer = StaffClassificationSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data, 'message': 'success'}) 
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
    
    def retrieve(self, request, pk=None):
        api_response = successMsg()
        try:
            id=pk
            if StaffClassification.objects.filter(pk=id).exists(): 
                obj = StaffClassification.objects.get(id=id)
                serializer = StaffClassificationSerializers(obj, many=False)
                return Response({'status':200,'data':serializer.data, 'message': 'Success'})
            else:
                return Response({'status':404, 'message': 'Staff does not exist at this position'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)

    def create(self, request):
        api_response = successMsg()
        try:
            serializer = StaffClassificationSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
        
    
    def update(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
        
            if StaffClassification.objects.filter(pk=id).exists(): 
                obj = StaffClassification.objects.get(pk=id)    
                serializer = StaffClassificationSerializers(obj, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status':400, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':404, 'message': 'Staff does not exist at thiSs index'}, status=status.HTTP_404_NOT_FOUND)  
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
                 


    def destroy(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
            if StaffClassification.objects.filter(pk=id).exists(): 
                obj = StaffClassification.objects.get(id=pk)
                if obj.is_active == False:
                    msg = "Staff is already deactivated"
                    return Response({'status':400, 'message':msg})
                serializer = StaffClassificationSerializers(obj, many=False)
                obj.is_active = False
                obj.save()
            
                return Response({'status':200, 'data': serializer.data, 'message': 'Successfully Deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': 'Staff does not exist at this index'}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)



class OrganizationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]

    def list(self, request):
        api_response = successMsg()
        try:
            obj = Organization.objects.all()
            serializer = OrganizationAndLocationSerializers(obj, many=True)
            return Response({'status': 200, 'data': serializer.data, 'message':'Success'})
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)

    def retrieve(self, request, pk=None):
        api_response = successMsg()
        try:
            id=pk
            if Organization.objects.filter(pk=id).exists():
                obj = Organization.objects.get(id=id)
                if obj.organization_is_active == False:
                    msg = "Please update the organization status to active"
                    return Response({'status':400, 'message': msg})
                serializer = OrganizationAndLocationSerializers(obj, many=False)
                return Response({'status':200, 'data':serializer.data, 'message':'Successfully added'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': "Organization does not exist in db"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'status': 404, 'message': 'Dynamic id entered into url is not of type int' })
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)
            


    def create(self, request):
        api_response = successMsg()
        try:
            city_name = request.data.get('city_name')
            locations = {'organization_id':1 , 'city_name': city_name}
            serializer = OrganizationSerializers(data = request.data)
            if serializer.is_valid():
                org = serializer.save()
                locations['organization_id'] = org.id
                lserializer = OrganizationLocationSerializers(data = locations)
                if lserializer.is_valid():
                    lserializer.save()
                    print(lserializer)
                print(org)
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully added'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':400, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)

    def update(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
            if Organization.objects.filter(pk=id).exists():
                obj = Organization.objects.get(pk=id)  
                serializer = OrganizationAndLocationSerializers(obj, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status':400, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':404, 'message': 'This Organization does not exists'})
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)

    def destroy(self, request, pk):
        api_response = successMsg()
        try:
            id = pk
            if Organization.objects.filter(pk=id).exists():
                obj = Organization.objects.get(id=pk)
                if obj.organization_is_active == False:
                    msg = "Organization is already deactivated"
                    return Response({'status':200, 'message':msg})
                obj.organization_is_active = False
                obj.save()
                serializer = OrganizationAndLocationSerializers(obj)
                return Response({'status':200, 'data': serializer.data, 'message': 'Deleted Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': 'This Organization does not exists'})
        except Exception as e:
            api_response['status'] = status.HTTP_400_BAD_REQUEST
            api_response['system_error_message'] = str(e)
            api_response['message'] = ''
            return Response(api_response)