from . import views
from django.urls import path
urlpatterns = [
    path(':', views.msg),
    path('gettest', views.getTest),
    path('inserttest', views.insertTest),
 ]