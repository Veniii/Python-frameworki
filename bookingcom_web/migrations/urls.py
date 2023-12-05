from django.urls import path
from bookingcom_web.views import test_response
urlpatterns = [
    path('test/', test_response),
]