from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        """Hanlde Updating Object partially"""
        return Response({'method':'patch'})
    def delete(self,request,pk=None):
        """Handle Delete an Object"""
        return Response({'method':'Delete'})
