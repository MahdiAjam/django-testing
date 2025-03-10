from rest_framework.views import APIView
from rest_framework.response import Response
from .mixins import LoggingMixins

class Home(LoggingMixins, APIView):
    def get(self, request):
        return Response('hello')
