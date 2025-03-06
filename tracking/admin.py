from django.contrib import admin
from .models import APIRequestLog

class APIRequestLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'request_at',
        'response_ms',
        'status_code',
        'user',
        'view_method',
        'path',
        'remote_address',
        'host',
        'query_params',
    )


admin.site.register(APIRequestLog, APIRequestLogAdmin)
