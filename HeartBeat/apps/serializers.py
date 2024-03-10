from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'password', 'email', 'phone_number', 'registration_date']
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','gender','name','discription','is_online',
                  'active_in_search','last_coordinates','contact_data','birth_day']
class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender_name']
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['profile','liked_profile']
class DisikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disike
        fields = ['profile','disliked_profile']
class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['first_profile','second_profile']
class PreferenceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceTag
        fields = ['name']
class ProfileTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileTag
        fields = ['profile','tag']
class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name']
class ProfileTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileTarget
        fields = ['profile','target']
        '''
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['profile','image_link']
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['user','device_name']
        '''