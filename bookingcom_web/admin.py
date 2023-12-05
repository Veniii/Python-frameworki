from django.contrib import admin
from .models import Article\
from django.urls import path
from bookingcom_web.views import test_response
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response),
]


# Register your models here.
admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "content", "year", "imgThumb"]
    exclude = ["content"]
    list_display = ["title", "year"]
    list_filter = ["year"]
    search_fields = ["title", "content"]