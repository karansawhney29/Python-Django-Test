from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers
# Create your views here.


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'http methods',
            'django view',
            'urls',
            'logical control'
        ]

        return Response({'message': 'Hello!', 'Api View List': an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):

        return Response({'method': 'put'})

    def patch(self, request, pk=None):

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    
    def list(self, request):
        a = [
            "onew",
            "two",
            "threee",
            "four"
        ]
        
        return Response({"message": "list", "viewSet": a})
