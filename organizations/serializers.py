from rest_framework import serializers
from .models import Organization, GroupHead

class CreateOrganizationSerializers(serializers.ModelSerializer):
    organization_logo = serializers.ImageField(required=False)
    class Meta:
        model = Organization
        fields = ['organization_name', 'organization_tagline', 'organization_vision', 'organization_mission', 'organization_logo','created_by', 'established_date', 'company_type']



class ViewOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
 
class UpdateOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['organization_name', 'organization_tagline', 'organization_vision', 'organization_mission', 'organization_logo','created_by', 'established_date', 'company_type', 'organization_is_active']


class DeactivateOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class CreateGroupHeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupHead
        exclude = ('created_at', 'updated_at')
        
    