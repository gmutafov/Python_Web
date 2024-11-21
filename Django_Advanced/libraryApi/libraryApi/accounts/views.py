from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from libraryApi.accounts.serializers import RegisterSerializer


# Create your views here.

UserModel = get_user_model()

class RegisterApiView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer

