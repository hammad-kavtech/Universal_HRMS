from rest_framework import serializers
from .models import Organization, GroupHead, OrganizationLocation, OrganizationDepartment, OrganizationPosition, StaffClassification

class OrganizationSerializers(serializers.ModelSerializer):
    organization_logo = serializers.ImageField(required=False)
    class Meta:
        model = Organization
        fields = '__all__'


class GroupHeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupHead
        fields = '__all__'


class OrganizationLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationLocation
        exclude =  '__all__'


class OrganizationDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDepartment
        exclude = '__all__'



class OrganizationPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPosition
        fields = '__all__'


class StaffClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffClassification
        fields = '__all__'