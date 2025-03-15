from rest_framework.views import APIView
from rest_framework.response import Response
from .mixins import LoggingMixins

class Home(LoggingMixins, APIView):
    sensitive_fields = {'pass'}

    # def should_log(self, request, response):
    #     return response.status_code >= 400

    def get(self, request):
        return Response('hello')
