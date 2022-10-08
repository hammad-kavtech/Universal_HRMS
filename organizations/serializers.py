from rest_framework import serializers
from .models import Organization, GroupHead, OrganizationLocation, OrganizationDepartment, OrganizationPosition, StaffClassification

# Serializer for Organization 
class CreateOrganizationSerializers(serializers.ModelSerializer):
    organization_logo = serializers.ImageField(required=False)
    class Meta:
        model = Organization
        fields = ['organization_name', 'organization_tagline', 'organization_vision', 'organization_mission', 'organization_logo','created_by', 'established_date', 'organization_type']

class ViewOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
 
class UpdateOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['organization_name', 'organization_tagline', 'organization_vision', 'organization_mission', 'organization_logo','created_by', 'established_date', 'organization_type', 'organization_is_active']


class DeactivateOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


# Serializer for organization GROUPHEAD
class CreateGroupHeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupHead
        exclude = ('created_at', 'updated_at')
        
class ViewGroupHeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupHead
        fields = '__all__'

class UpdateGroupHeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupHead
        exclude = ('created_at', 'updated_at', 'id')

class DeactivateGroupHeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupHead
        fields = '__all__'



# Serializer for Organization Location
class CreateOrganizationLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationLocation
        exclude =  ('created_at', 'updated_at')

class UpdateOrganizationLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationLocation
        exclude =  ('created_at', 'updated_at', 'id')

class ViewOrganizationLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationLocation
        fields = '__all__'

class DeactivateOrganizationLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationLocation
        fields = '__all__'



# Serializer for Organization Department
class CreateOrganizationDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDepartment
        exclude =  ('created_at', 'updated_at')

class UpdateOrganizationDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDepartment
        exclude =  ('created_at', 'updated_at', 'id')

class ViewOrganizationDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDepartment
        fields = '__all__'

class DeactivateOrganizationDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDepartment
        fields = '__all__'



# Serializers for Organization Positions
class CreateOrganizationPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPosition
        exclude =  ('created_at', 'updated_at')

class UpdateOrganizationPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPosition
        exclude =  ('created_at', 'updated_at', 'id')

class ViewOrganizationPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPosition
        fields = '__all__'

class DeactivateOrganizationPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPosition
        fields = '__all__'


# Serializers for Staff Classification
class CreateStaffClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffClassification
        exclude =  ('created_at', 'updated_at')

class UpdateStaffClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffClassification
        exclude =  ('created_at', 'updated_at', 'id')

class ViewStaffClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffClassification
        fields = '__all__'

class DeactivateStaffClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffClassification
        fields = '__all__'