from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
