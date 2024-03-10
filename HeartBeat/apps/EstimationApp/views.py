from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import *
from  ..serializers import *


# Create your views here.
class LikeView(APIView):
    def put(self, request):
        profile_id = request.data.get('profile') or request.query_params.get('profile')
        liked_profile_id = request.data.get('liked_profile') or request.query_params.get('liked_profile')
        # Add search by login and user_id
        if not all((profile_id, liked_profile_id)):
            return Response({'error': "Null values"}, status=422)

        try:
            Profile.objects.get(id=profile_id,active_in_search=True),
            Profile.objects.get(id=liked_profile_id,active_in_search=True)
        except:
            return Response({'error': "Profile not found"}, status=422)

        try:
            Like.objects.get(profile=profile_id,liked_profile=liked_profile_id)
            return Response({'error': "Like already exist"}, status=422)
        except:
            pass

        connection_created = False
        try:
            Like.objects.get(profile=liked_profile_id,liked_profile=profile_id)
            #Create Matched
            print("try match")
            connection_created = ConnectionView.createConnection(profile_id,liked_profile_id)
        except:
            pass


        like = LikeSerializer(data=request.data)
        if not like.is_valid():
            return Response(like.errors, status=422)
        like.save()
        if connection_created:
            return Response({'message': "Matched"}, status=201)
        return Response(like.data, status=201)
    def delete(self, request):
        profile_id = request.data.get('profile') or request.query_params.get('profile')
        liked_profile_id = request.data.get('liked_profile') or request.query_params.get('liked_profile')
        if not all((profile_id, liked_profile_id)):
            return Response({'error': "Null values"}, status=422)

        try:
            Like.objects.get(profile=profile_id,liked_profile=liked_profile_id).delete()
        except:
            return Response({'error': "Like not found"}, status=422)
        return Response({'message': "Like deleted"}, status=201)
class DislikeView(APIView):
    def put(self, request):
        profile_id = request.data.get('profile') or request.query_params.get('profile')
        disliked_profile_id = request.data.get('disliked_profile') or request.query_params.get('disliked_profile')
        # Add search by login and user_id
        if not all((profile_id, disliked_profile_id)):
            return Response({'error': "Null values"}, status=422)

        try:
            Profile.objects.get(id=profile_id,active_in_search=True),
            Profile.objects.get(id=disliked_profile_id,active_in_search=True)
        except:
            return Response({'error': "Profile not found"}, status=422)

        try:
            Disike.objects.get(profile=profile_id,disliked_profile=disliked_profile_id)
            return Response({'error': "Dislike already exist"}, status=422)
        except:
            pass

        dislike = DisikeSerializer(data=request.data)
        if not dislike.is_valid():
            return Response(dislike.errors, status=422)
        dislike.save()
        return Response(dislike.data, status=201)
    def delete(self, request):
        profile_id = request.data.get('profile') or request.query_params.get('profile')
        disliked_profile_id = request.data.get('disliked_profile') or request.query_params.get('disliked_profile')
        # Add search by login and user_id
        if not all((profile_id, disliked_profile_id)):
            return Response({'error': "Null values"}, status=422)

        try:
            Disike.objects.get(profile=profile_id,disliked_profile=disliked_profile_id).delete()
        except:
            return Response({'error': "Dislike not found"}, status=422)
        return Response({'message': "Dislike deleted"}, status=201)
class ConnectionView(APIView):
    def connection_validation(first_profile_id,second_profile_id):
        print("Connection validation")
        if not all((first_profile_id, second_profile_id)):
            print("Null values")
            return False
        print("Not null values")
        try:
            Connection.objects.get(first_profile=first_profile_id,second_profile=second_profile_id)
            print("Connection already exist")
            return False
        except:
            pass
        print("Connection not exist")
        try:
            Connection.objects.get(first_profile=second_profile_id,second_profile=first_profile_id)
            print("Connection already exist")
            return False
        except:
            pass
        print("Connection not exist")
        return True
    def createConnection(first_profile_id,second_profile_id):
        if not ConnectionView.connection_validation(first_profile_id,second_profile_id):
            print("false")
            return False
        print("Connection can be created")
        connection = ConnectionSerializer(data={"first_profile":second_profile_id,"second_profile":first_profile_id})
        print("Connection created")
        if not connection.is_valid():
            print("Connection not valid")
            return False
        connection.save()
        print("Connection saved")
        return True

    def put(self, request):
        first_profile_id = request.data.get('first_profile') or request.query_params.get('first_profile')
        second_profile_id = request.data.get('second_profile') or request.query_params.get('second_profile')

        if not ConnectionView.connection_validation(first_profile_id,second_profile_id):
            return Response({'error': "Connection already exist"}, status=422)

        connection = ConnectionSerializer(data=request.data)
        if not connection.is_valid():
            return Response(connection.errors, status=422)
        connection.save()
        return Response(connection.data, status=201)