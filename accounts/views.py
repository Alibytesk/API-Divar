#django
from django.shortcuts import render
#rest
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#apps
from .serializers import *
from .models import *


class ProfileView(APIView):

    def get(self, request):
        user = request.user
        serializer = UserSerializer(instance=user, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)