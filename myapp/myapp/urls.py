from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('funding.urls')),
    path('administrator/', admin.site.urls),
]
