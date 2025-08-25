from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.serializers import UserRegistrationSerializer

# Create your views here.
class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            return Response({"msg":"resgister successful"},
                            status)
        return Response({"msg":"resgister successful"})