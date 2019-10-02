from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('funding.urls')),
    path('funding/administrator/', admin.site.urls),
]
