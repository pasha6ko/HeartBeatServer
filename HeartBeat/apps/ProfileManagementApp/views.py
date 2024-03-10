from rest_framework.response import Response
from rest_framework.views import APIView

from ..TagManagmentApp.views import *
from ..serializers import *
from ..validator import Validator



class CreateProfileView(APIView):
    def put(self, request):
        # разные варианты регистрации
        user_id = request.data.get('user') or request.query_params.get('user')
        login = request.data.get('login') or request.query_params.get('login')

        name = request.data.get('name') or request.query_params.get('name')
        discription = request.data.get('discription') or request.query_params.get('discription')
        contact_data = request.data.get('contact_data') or request.query_params.get('contact_data')
        tags_list = request.data.get('tags') or request.query_params.get('tags')
        birth_day = request.data.get('birth_day') or request.query_params.get('birth_day')
        gender_id = request.data.get('gender') or request.query_params.get('gender')

        if not all((name, discription, contact_data, birth_day,gender_id,tags_list)):
            return Response({'error': "Null values"}, status=422)

        if user_id and login == None:
            return Response({'error': "Null values"}, status=422)
        elif user_id == None:
            user = User.objects.get(login=login)
            user_id = user.id
            request.data['user'] = user_id

        try:
            serializer = Profile.objects.get(user=user_id, active_in_search=True)
            return Response({'error': "Profile already exist"}, status=422)
        except:
            pass

        if not Validator.profile_name_validation(name):
            return Response({'error': "Uncorrect name"}, status=422)

        if not Validator.age_validation(birth_day):
            return Response({'error': "Unavaliable age"}, status=422)

        if not Validator.contact_data_validation(contact_data):
            return Response({'error': "Uncorrect contact data"}, status=422)

        try:
            gender = Gender.objects.get(id=gender_id)
        except:
            return Response({'error': "Gender not found"}, status=422)


        serializer = ProfileSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=422)  # Change Status code



        profile =  serializer.save()

        profile_id = profile.id
        #create tags
        tags_list = tags_list.split(',')
        for tag in tags_list:
            try:
                tag = PreferenceTag.objects.get(id=int(tag))
            except:
                return Response({'error': "Tag not found"}, status=422)

        if not ProfileTagView.create_tags(profile_id, tags_list):
            return Response({'error': "tags create error"}, status=422)

        return Response(serializer.data, status=201)
    def delete(self,request):
        user_id = request.data.get('user') or request.query_params.get('user')
        login = request.data.get('login') or request.query_params.get('login')

        if user_id and login == None:
            return Response({'error': "Null values"}, status=422)
        elif user_id == None:
            user = User.objects.get(login=login)
            user_id = user.id
        try:
            profile = Profile.objects.get(user=user_id)
        except:
            return Response({'error': "Profile not found"}, status=422)

        profile.delete()
        return Response(status=204)
class ProfileInteractionView(APIView):
    def get(self, request):
        user_id = request.data.get('user') or request.query_params.get('user')
        login = request.data.get('login') or request.query_params.get('login')

        if user_id and login == None:
            return Response({'error': "Null values"}, status=422)
        elif user_id == None:
            user = User.objects.get(login=login)
            user_id = user.id
            print(user_id)

        try:
            profile = Profile.objects.get(user=user_id) # rework to get many profiles
        except:
            return Response({'error': "Profile not found"}, status=422)

        return Response(ProfileSerializer(profile).data, status=201)

    def post(self, request):
        user_id = request.data.get('user') or request.query_params.get('user')
        login = request.data.get('login') or request.query_params.get('login')

        if user_id and login == None:
            return Response({'error': "Null values"}, status=422)
        elif user_id == None:
            user = User.objects.get(login=login)
            user_id = user.id

        try:
            profile = Profile.objects.get(user=user_id)
        except:
            return Response({'error': "Profile not found"}, status=422)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=422)  # Change Status code

        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        user_id = request.data.get('user') or request.query_params.get('user')
        login = request.data.get('login') or request.query_params.get('login')

        if user_id and login == None:
            return Response({'error': "Null values"}, status=422)
        elif user_id == None:
            user = User.objects.get(login=login)
            user_id = user.id

        try:
            profile = Profile.objects.get(user=user_id)
        except:
            return Response({'error': "Profile not found"}, status=422)

        profile.delete()
        return Response(status=204)
