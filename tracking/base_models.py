from django.db import models
from django.conf import settings

class BaseAPIRequestLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    username_persistent = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_USERNAME_LENGTH', 200), null=True,
                                           blank=True)
    request_at = models.DateTimeField(db_index=True)
    response_ms = models.PositiveIntegerField(default=0)
    path = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_PATH_LENGTH', 200), db_index=True,
                            help_text='url path')
    view = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_VIEW_LENGTH', 200), null=True, blank=True,
                            db_index=True, help_text='method called by this endpoint')  # the class has been called
    view_method = models.CharField(max_length=getattr(settings, 'DRF_TRACKING_VIEW_METHOD_LENGTH', 200), null=True,
                                   blank=True, db_index=True)  # what method in class has been called. "get"
    remote_address = models.GenericIPAddressField()
    host = models.URLField()
    method = models.CharField(max_length=10)  # the HTTP method "GET"
    query_params = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    errors = models.TextField(null=True, blank=True)
    status_code = models.PositiveIntegerField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
        verbose_name = 'API Request Log'

    def __str__(self):
        return '{} {}'.format(self.method, self.path)
