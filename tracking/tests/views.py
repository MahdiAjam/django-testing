from rest_framework.views import APIView
from rest_framework.response import Response
from tracking.mixins import LoggingMixins


class MockNoLoggingView(APIView):
    def get(self, request):
        return Response('No logging')


class MockLoggingView(LoggingMixins, APIView):
    def get(self, request):
        return Response('With logging')
