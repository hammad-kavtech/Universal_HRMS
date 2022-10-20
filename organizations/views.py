from asyncio.windows_events import NULL
from django.forms import IntegerField
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from helpers.renderers import Renderer
from organizations.models import Organization, GroupHead, OrganizationLocation, OrganizationDepartment, StaffClassification
from .serializers import GroupHeadSerializers, OrganizationAndLocationSerializers, OrganizationSerializers, OrganizationLocationSerializers, OrganizationDepartmentSerializers, StaffClassificationSerializers, OrganizationAndLocationSerializers
from rest_framework.parsers import MultiPartParser, FormParser
import numpy as np
from helpers.errorHandling import exception
# Create your views here.

def activator(model_name, serializer_name, name, pk):
    if model_name.objects.filter(id=pk).exists():  
        obj = model_name.objects.get(id=pk)
        if obj.is_active == True:
            return Response({'status':404, 'message': 'It is already activated'})
        
        obj.is_active=True
        obj.save()
        serializer = serializer_name(obj, many=False)
        return Response({'status':200, 'data':serializer.data, 'message': 'Successfully Activated'})
    else:
        return Response({'status':404, 'message': 'This Organization does not exists'})

class OrganizationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]
    parser_classes = [MultiPartParser, FormParser]

    @action(methods=['PATCH'], detail=True)
    def activateOrganization(self, request, pk):
        try:  
            return activator(Organization, OrganizationSerializers, pk)
        except Exception as e:
            return exception(e)


    def list(self, request):
        try:
            obj = Organization.objects.filter(is_active=True)
            serializer = OrganizationAndLocationSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data, 'message': 'Success'})
        except Exception as e:
            return exception(e)

    def retrieve(self, request, pk=None):
        try:
            if Organization.objects.filter(id=pk).exists():
                obj = Organization.objects.get(id=pk)
                if obj.is_active == False:
                    msg = "Please update the organization status to active"
                    return Response({'status':400, 'message': msg})
                serializer = OrganizationAndLocationSerializers(obj, many=False)
                return Response({'status':200, 'data':serializer.data, 'message':'Successfully added'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': "Organization does not exist in db"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'status': 404, 'message': 'Dynamic id entered into url is not of type int' })
        except Exception as e:
            return exception(e)
            


    def create(self, request):
        try:
            location_data = {'organization':'', 'address':'', 'city_name':'', 'longitute':'', 'latitute':''}
            location_data['address'] = request.data.get('address') or None
            location_data['city_name'] = request.data.get('city_name') or None
            location_data['longitute'] = request.data.get('longitute') or None
            location_data['latitute'] = request.data.get('latitute') or None
            serializer = OrganizationSerializers(data = request.data)
            if serializer.is_valid():
                org = serializer.save()
                location_data['organization'] = org.id
                
                lserializer = OrganizationLocationSerializers(data = location_data)
                if lserializer.is_valid():
                    lserializer.save()
                    obj = Organization.objects.get(id=org.id)
                    org_serializer = OrganizationAndLocationSerializers(obj, many=False)
                    
                    return Response({'status':201, 'data':org_serializer.data, 'message':'Successfully added'}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'status':400, 'message': lserializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':400, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return exception(e)

    def update(self, request, pk):
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
            return exception(e)

    def destroy(self, request, pk):
        try:
            id = pk
            if Organization.objects.filter(pk=id).exists():
                obj = Organization.objects.get(id=pk)
                if obj.is_active == False:
                    msg = "Organization is already deactivated"
                    return Response({'status':200, 'message':msg})
                obj.is_active = False
                obj.save()
                serializer = OrganizationAndLocationSerializers(obj)
                return Response({'status':200, 'data': serializer.data, 'message': 'Deleted Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'status':404, 'message': 'This Organization does not exists'})
        except Exception as e:
            return exception(e)




# Group head logic
class GroupHeadViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]
    queryset = GroupHead.objects.filter(is_active=True, organization__is_active=True)
    def list(self, request):
        try:    
            obj = GroupHead.objects.filter(is_active=True, organization__is_active=True)
            serializer = GroupHeadSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data, 'message': 'Success'})
        except Exception as e:
            return exception(e)


    def retrieve(self, request, pk=None):
        try:
            id=pk
            if GroupHead.objects.filter(pk=id).exists():
                obj = GroupHead.objects.get(id=id)
                if obj.organization.is_active == False:
                    return Response({'status':400,'message': 'Change the status of organization to active first'})
                if obj.is_active == False:
                    return Response({'status':400,'message': 'Change the status of grouphead to active first'})
                serializer = GroupHeadSerializers(obj, many=False)
                return Response({'status':200,'data':serializer.data, 'message': 'Success'})
            else:
                return Response({'status':404, 'message': 'This Grouphead does not exists in database'})   
        except Exception as e:
            return exception(e)
     

    def create(self, request):
        try:
            serializer = GroupHeadSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return exception(e)
        
    
    def update(self, request, pk):
        try:
            id = pk
            
            if GroupHead.objects.filter(pk=id).exists():
                obj = GroupHead.objects.get(pk=id)    
                if obj.organization.is_active == False:
                    return Response({'status':400,'message': 'Change the status of organization to active first'})
                if obj.is_active == False:
                    return Response({'status':400,'message': 'Change the status of grouphead to active first'})
                serializer = GroupHeadSerializers(obj, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status':400, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':404, 'message': 'Grouphead with this index does not exist in db'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return exception(e)

    def destroy(self, request, pk):
        try:
            id = pk
            if GroupHead.objects.filter(pk=id).exists():
                obj = GroupHead.objects.get(id=id)
                if obj.organization.is_active == False:
                    return Response({'status':400,'message': 'Change the status of organization to active first'})
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
            return exception(e)




# organization Department Logic
class OrganizationDepartmentViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # renderer_classes = [Renderer]
    def list(self, request):
        try:
            obj = OrganizationDepartment.objects.filter( is_active = True, grouphead__is_active=True, grouphead__organization__is_active=True)
            serializer = OrganizationDepartmentSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data, 'message': 'Success'})
        except Exception as e:
            return exception(e)
    

    def retrieve(self, request, pk=None):
        try:  
            if OrganizationDepartment.objects.filter(id=pk).exists():
                obj = OrganizationDepartment.objects.get(id=pk)
                if obj.is_active == False:
                    return Response({'status':400,'message': 'Change the status of the department to active first'})  
                # obj_dep = OrganizationDepartment.objects.filter(grouphead_id__in = GroupHead.objects.filter(organization_id=obj_org.id).values_list('id', flat = True))
                serializer = OrganizationDepartmentSerializers(obj, many=False)
                return Response({'status':200, 'data':serializer.data, 'message': 'Success'})
            else:
                return Response({'status':404, 'message': "Department does not exist at this index"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return exception(e)

    def create(self, request):
        try:
            serializer = OrganizationDepartmentSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return exception(e)
        
    
    def update(self, request, pk):
        try:
            id = pk

            if OrganizationDepartment.objects.filter(pk=id).exists():    
                obj = OrganizationDepartment.objects.get(pk=id) 
                # if obj.is_active == False:
                #     return Response({'status':400,'message': 'Change the status of the department to active first'})    
                serializer = OrganizationDepartmentSerializers(obj, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status':200, 'data': serializer.data, 'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status':404, 'message': "Department does not exist at this index"}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            return exception(e)



    def destroy(self, request, pk):
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
            return exception(e)
            


# staff classification viewset
class StaffClassificationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # prenderer_classes = [Renderer]
    def list(self, request):   
        try:
            obj = StaffClassification.objects.filter(is_active=True, organization__is_active=True)
            serializer = StaffClassificationSerializers(obj, many=True)
            return Response({'status':200,'data':serializer.data, 'message': 'Success'})
        except Exception as e:
            return exception(e)  
    
    def retrieve(self, request, pk=None):
        try:
            if StaffClassification.objects.filter(id=pk).exists(): 
                obj = StaffClassification.objects.get(id=pk)
                serializer = StaffClassificationSerializers(obj, many=False)
                return Response({'status':200,'data':serializer.data, 'message': 'Success'})
            else:
                return Response({'status':404, 'message': 'Staff does not exist at this position'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return exception(e)

    def create(self, request):
        try:
            serializer = StaffClassificationSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201, 'data':serializer.data, 'message':'Successfully created'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status':404, 'message':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return exception(e)
        
    
    def update(self, request, pk):
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
            return exception(e)
                 


    def destroy(self, request, pk):
        try:
            if StaffClassification.objects.filter(id=pk).exists(): 
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
            return exception(e)



class OrganizationDashboardViewset(viewsets.ModelViewSet):

    # @action(methods=['GET'], detail=True)
    # def active(self, request, pk):
    #     try:    
    #         obj = Organization.objects.filter(is_active=True)
    #         serializer = OrganizationSerializers(obj, many=True)
    #         return Response({'status':200, 'data':serializer.data, 'message': 'Success'})
    #     except Exception as e:
    #         return exception(e)

    # @action(methods=['GET'], detail=True)
    # def deactive(self, request, pk):
    #     try:    
    #         obj = Organization.objects.filter(is_active=False)
    #         serializer = OrganizationSerializers(obj, many=True)
    #         return Response({'status':200, 'data':serializer.data, 'message': 'Success'})
    #     except Exception as e:
    #         return exception(e)

    # @action(methods=['GET'], detail=True)
    # def all(self, request, pk):
    #     try:    
    #         obj = Organization.objects.all()
    #         serializer = OrganizationSerializers(obj, many=True)
    #         return Response({'status':200, 'data':serializer.data, 'message': 'Success'})
    #     except Exception as e:
    #         return exception(e)


    def retrieve(self, request, pk=None):  

        try:
            
            obj_org = Organization.objects.filter(user_id=pk, is_active=True)[:1].get()
            
            # if len(obj_org) > 1:
            #     return Response({'status': 400, 'message': 'More than one organization is activated'})

            # obj_org = Organization.objects.get(id=1)
            
            serializer_org = OrganizationAndLocationSerializers(obj_org, many=False)
            obj_gh = GroupHead.objects.filter(organization_id=obj_org.id )
            serializer_gh = GroupHeadSerializers(obj_gh, many=True)
            total_grouphead = len(serializer_gh.data)
            obj_sc = StaffClassification.objects.filter(organization_id = obj_org.id)
            serializer_sc = StaffClassificationSerializers(obj_sc, many=True)
            total_staffclassification = len(serializer_sc.data)
            obj_dep = OrganizationDepartment.objects.filter(grouphead_id__in = GroupHead.objects.filter(organization_id=obj_org.id).values_list('id', flat = True))
            serializer_dep = OrganizationDepartmentSerializers(obj_dep, many=True)
            total_department = len(serializer_dep.data)

            data = {'organization': serializer_org.data, 'total grouphead': total_grouphead, 'grouphead': serializer_gh.data, 'total_staffclassifcation': total_staffclassification, 'staff classification': serializer_sc.data, 'total department':total_department, 'department': serializer_dep.data}
            return Response({'status':200,'data': data, 'message': 'success'}) 

        except Exception as e:
            return exception(e)