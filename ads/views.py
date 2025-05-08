from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from .permissions import *
from .paginations import *
from .models import *

class AdListView(APIView, StandardResultSetPagination):
    serializer_class = AdSerializer
    parser_classes = (MultiPartParser,)
    def get(self, request):
        queryset = Ad.objects.filter(is_public=True)
        result = self.paginate_queryset(queryset, request)
        serializer = AdSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class AdCreateView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = AdSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdDetailView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsPublisherOrReadOnly,]
    parser_classes = (MultiPartParser,)
    def get_object(self):
        _object = get_object_or_404(klass=Ad, id=self.kwargs['pk'])
        self.check_object_permissions(obj=_object, request=self.request)
        return _object

    def get(self, request, pk=None):
        _object = self.get_object()
        serializer = AdSerializer(instance=_object, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        _object = self.get_object()
        serializer = AdSerializer(
            data=request.data,
            instance=_object,
            many=False,
            partial=True
        )
        if serializer.is_valid():
            serializer.update(instance=_object, validated_data=serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


