from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import UserSerializer
from ..models import User



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def get(self, request):
        id = request.data.get('id') or request.query_params.get('id')
        if id is None:
            return Response(status=400)
        try:
            user = User.objects.get(id = id)
            userData = UserSerializer(user).data
            return Response(userData, status=201)
        except:
            return Response(status=400)
    def put(self,request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

