from rest_framework import serializers
from .models import organization
from xml.dom import ValidationErr
from django.forms import ValidationError

class CreateOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = ['organization_name', 'organization_tagline', 'organization_vision', 'organization_mission', 'organization_logo','created_by', 'established_date', 'company_type']

        def validate(self, attrs):

            return attrs

class ViewOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = '__all__'
 
        

class UpdateOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = ['organization_name', 'organization_tagline', 'organization_vision', 'organization_mission', 'organization_logo','created_by', 'established_date', 'company_type', 'organization_is_active']

    def validate(self, attrs):
        

        return attrs

class DeactivateOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = '__all__'

