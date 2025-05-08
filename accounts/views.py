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
    serializer_class = UserSerializer
    def get(self, request):
        user = request.user
        serializer = UserSerializer(instance=user, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(data=request.data, partial=True, instance=user, many=False)
        if serializer.is_valid():
            serializer.update(validated_data=serializer.validated_data, instance=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)