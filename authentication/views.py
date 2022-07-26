from tkinter.messagebox import RETRY
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import response, status

from authentication.serializers import RegisterSerializers


# Create your views here.
class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializers

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status = status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)