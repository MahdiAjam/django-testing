# drf-api-tracking

`drf-api-tracking` is a Django and DRF package that logs Django Rest Framework requests to the database. This package provides a Django model and a DRF view mixin that work together to track request/response details for improved monitoring and debugging.

## Features
- Logs detailed information about each request and response cycle.
- Captures both authenticated and unauthenticated requests.
- Preserves the username even after the related `User` object is deleted.
- Tracks key request/response data including:
  - **Request Timing:** Measures the milliseconds spent processing the request in the view.
  - **User Details:** Captures the authenticated user or maintains the username persistently if deleted.
  - **Request and Response Data:** Logs query parameters, POST data, and JSON response content for thorough insights.
  - **HTTP Metadata:** Tracks the method, status code, and originating IP address.
- Includes robust support for both function-based views and class-based views.
- Provides clear insights for debugging, performance monitoring, and analytics.

## Usage

### Step 1: Add the Mixin to Your DRF Views
To start tracking requests, add the `ApiLoggingMixin` to your DRF views or viewsets:

```python
from drf_api_tracking.mixins import ApiLoggingMixin
from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleView(ApiLoggingMixin, APIView):
    def get(self, request):
        return Response({"message": "This is a tracked endpoint."})
```

### Step 2: Model Overview
The package provides a model called `APIRequestLog` with the following fields:

| Field Name         | Description                                              | Field Type           |
|--------------------|----------------------------------------------------------|----------------------|
| `user`              | User if authenticated, None if not                        | ForeignKey            |
| `username_persistent` | Static field that persists username even if `User` is deleted | CharField              |
| `requested_at`      | Date-time that the request was made                      | DateTimeField         |
| `response_ms`       | Number of milliseconds spent in view code               | PositiveIntegerField  |
| `path`               | Target URI of the request                                | CharField              |
| `view`               | Target VIEW of the request                              | CharField              |
| `view_method`        | Target METHOD of the VIEW                               | CharField              |
| `remote_addr`        | IP address where the request originated                 | GenericIPAddressField  |
| `host`               | Originating host of the request                         | URLField               |
| `method`             | HTTP method (e.g., GET, POST)                          | CharField              |
| `query_params`       | Dictionary of request query parameters (as text)        | TextField              |
| `data`               | Dictionary of POST data (JSON or form)                  | TextField              |
| `response`           | JSON response data                                       | TextField              |
| `status_code`        | HTTP status code                                         | PositiveIntegerField  |

## Configuration

You can customize the following settings in your `settings.py` file:
```python
API_TRACKING_SETTINGS = {
    "LOG_DATA": True,  # Whether to log request/response data
    "EXCLUDE_PATHS": ["/health/", "/metrics/"],  # Paths to exclude from logging
}
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please submit issues or pull requests to improve the package.

## Contact
For questions, feel free to reach out via the project's GitHub repository.

