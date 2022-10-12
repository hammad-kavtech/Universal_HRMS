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
        fields =  '__all__'


class OrganizationDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDepartment
        fields = '__all__'



class OrganizationPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPosition
        fields = '__all__'


class StaffClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffClassification
        fields = '__all__'


class UpdateStaffClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffClassification
        fields = '__all__'


class OrganizationAndLocationSerializers(serializers.ModelSerializer):
    locations = OrganizationLocationSerializers(many=True) 
    organization_logo = serializers.ImageField(required=False)
    


    def create(self, validated_data):
        city_name = validated_data.get('city_name')
        print(city_name)
        locations = [{'city_name': city_name}]
        validated_data.pop("city_name")
        validated_data['locations'] = locations
        print(validated_data)
        return validated_data




    class Meta:
        model = Organization
        fields = '__all__' 

    