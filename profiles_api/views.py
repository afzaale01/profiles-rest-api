from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, response=None):
        """Return a list of APIView features"""
        an_apiview =[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View ',
            'Gives you the most control over your appication logic',
            'Is mapped manually to URls',
        ]

# we retutn a list or and dictionry as Response
        return Response({'massage':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello massage with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = f'Hello {name}'
            return Response({'massage':massage})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle Updating an Object"""
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        """Handle Updating Object partially"""
        return Response({'method':'patch'})
    def delete(self,request,pk=None):
        """Handle Delete an Object"""
        return Response({'method':'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    def list(self,request):
        """Return Some String for massage passing test"""

        a_viewset = [
                        'Uses actions (list, create, retrieve, update, partial_update)',
                        'Automatically maps to URLs using Routers',
                        'Provides more functionality with less code',
                    ]

        return Response({'massage':'Hello!','a_viewset':a_viewset})
