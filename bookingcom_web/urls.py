from django.urls import path
from bookingcom_web.views import test_response, all_articles

urlpatterns = [
    path('test/', test_response),
    path('test/all_articles/', all_articles)
]