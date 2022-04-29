from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    '''test api view'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        ''' returns list of apiview features'''
        an_apiview = [
            'uses http methods as function (get, post patch, put, delete)',
            'is similiar to a traditional django view',
            'gives you the control over app logic',
            'another one',
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})

    def post(self, request):
        '''create a hello message'''
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,)

    def put(self, request, pk=None):
        '''handle updating an object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''handle a partial update of an object'''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        '''delete an object'''
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
         'uses actions (list....)',
         'more functionalisty'
        ]

        return Response({'message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''handle geting object by ID'''
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        return  Response({'http_method': 'DELETE'})
