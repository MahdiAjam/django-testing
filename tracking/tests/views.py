from rest_framework.views import APIView
from rest_framework.response import Response
from tracking.mixins import LoggingMixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


class MockNoLoggingView(APIView):
    def get(self, request):
        return Response('No logging')


class MockLoggingView(LoggingMixins, APIView):
    def get(self, request):
        return Response('With logging')


class MockExplicitLoggingView(LoggingMixins, APIView):
    logging_methods = ['POST']

    def get(self, request):
        return Response('No logging')

    def post(self, request):
        return Response('With logging')


class MockCustomCheckLoggingView(LoggingMixins, APIView):
    def should_log(self, request, response):
        return 'log' in response.data

    def get(self, request):
        return Response('With logging')

    def post(self, request):
        return Response('No recording')


class MockSessionAuthLoggingView(LoggingMixins, APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response('With session auth logging')


class MockTokenAuthLoggingView(LoggingMixins, APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, reqeust):
        return Response('With token auth logging')


class MockSensitiveFieldsLoggingView(LoggingMixins, APIView):
    sensitive_fields = {'mY_fiElD'}

    def get(self, request):
        return Response('With logging')


class MockInvalidCleanedSubstituteLoggingView(LoggingMixins, APIView):
    CLEANED_SUBSTITUTE = 1

