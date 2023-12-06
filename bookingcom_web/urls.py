from django.urls import path
from bookingcom_web.views import all_articles

urlpatterns = [
    path('test/', all_articles),
]