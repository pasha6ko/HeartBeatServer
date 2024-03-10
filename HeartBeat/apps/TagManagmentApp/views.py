from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import PreferenceTag
from ..serializers import *


# Create your views here.
class ProfileTagView(APIView):
    def delet_all_tags_for_profile(profile_id):
        tags = ProfileTag.objects.filter(profile=profile_id)
        for tag in tags:
            tag.delete()
    def create_tag_for_profile(profile_id,tag):
        profile_tag = ProfileTagSerializer(data={'profile':profile_id,'tag':int(tag)})
        print(f"tag: {tag}, profile_id: {profile_id}")
        if not profile_tag.is_valid():
            print("tag not valid")
            return False
        profile_tag.save()
        print("tag created")
        return True
        pass
    def create_tags(profile_id,tags_list):
        for tag in tags_list:
            if not ProfileTagView.create_tag_for_profile(profile_id,tag):
                return False # delete all
        return True
