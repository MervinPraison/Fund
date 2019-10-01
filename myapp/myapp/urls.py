from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('funding/', include('funding.urls')),
    path('admin/', admin.site.urls),
]