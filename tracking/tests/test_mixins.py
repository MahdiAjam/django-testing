from rest_framework.test import APITestCase, APIRequestFactory
from tracking.models import APIRequestLog
from .views import MockLoggingView
from django.test import override_settings


@override_settings(ROOT_URLCONF='tracking.tests.urls')
class TestLoggingMixin(APITestCase):
    def test_nologging_no_log_created(self):
        self.client.get('/no-logging/')
        self.assertEqual(APIRequestLog.objects.all().count(), 0)

    def test_logging_creates_log(self):
        self.client.get('/logging/')
        self.assertEqual(APIRequestLog.objects.all().count(), 1)
