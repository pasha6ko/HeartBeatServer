from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import *
from ..validator import Validator


class CreateProfileView(APIView):
    def put(self, request):
        user_id = request.data.get('user_id') or request.query_params.get('user_id')
        name = request.data.get('name') or request.query_params.get('name')
        discription = request.data.get('discription') or request.query_params.get('discription')
        contact_data = request.data.get('contact_data') or request.query_params.get('contact_data')
        birth_date = request.data.get('birth_date') or request.query_params.get('birth_date')
        print(name)
        print(discription)
        print(contact_data)
        print(birth_date)
        print(user_id)

        if not all((user_id, name, discription, contact_data, birth_date)):
            return Response({'error': "Null values"}, status=422)

        if not Validator.profile_name_validation(name):
            return Response({'error': "Uncorrect name"}, status=422)

        if not Validator.age_validation(birth_date):
            return Response({'error': "Unavaliable age"}, status=422)

        if not Validator.contact_data_validation(contact_data):
            return Response({'error': "Uncorrect contact data"}, status=422)

        serializer = ProfileSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=422)  # Change Status code

        serializer.save()
        return Response(serializer.data, status=201)
