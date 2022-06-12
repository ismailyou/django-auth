from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import UserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        if data["password"] != data["password_confirm"]:
            raise exceptions.APIException("password do not match !")

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return  Response(serializer.data)









