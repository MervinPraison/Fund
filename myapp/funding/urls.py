from django.urls import path

from . import views

app_name = 'funding'

urlpatterns = [
    # ex: /funding/
    path('', views.index, name='index'),
    path('newcall/', views.newcall, name='newcall'),
    # ex: /funding/1/
    path('<int:fund_id>/', views.detail, name='detail'),
]