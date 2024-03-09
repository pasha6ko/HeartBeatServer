from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UserSerializer
from ..models import User
from ..validator import Validator


# Create your views here.
class SighInView(APIView):
    def get(self,request):

        login = request.data.get('login') or request.query_params.get('login')
        password = request.data.get('password') or request.query_params.get('password')

        if login or password == None:
            return Response("Неверный логин или пароль",status=422)

        user = User.objects.get(login = login)
        userData = UserSerializer(user).data

        if user == None:
            return Response({"error":"Uncorrect login or password"},status=422)

        if password != userData.get('password'):
            return Response({"error":"Uncorrect login or password"},status=422)

        userData = UserSerializer(user).data
        return Response(userData,status=201)


class RegisterView(APIView):
    def put(self,request):

        login = request.data.get('login') or request.query_params.get('login')
        password = request.data.get('password') or request.query_params.get('password')
        phone_number = request.data.get('phone_number') or request.query_params.get('phone_number')
        email = request.data.get('email') or request.query_params.get('email')

        if not all((login, password, phone_number, email)):
            return Response({'error':"Null values"},status=422)

        if not Validator.check_phone_number(phone_number):
            return Response({'error':"Uncorrect phone"},status=422)

        if not Validator.check_email(email):
            return Response({'error':"Uncorrect email"},status=422)

        if not Validator.password_validation(password):
            return Response({'error':"Uncorrect password"},status=422)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
