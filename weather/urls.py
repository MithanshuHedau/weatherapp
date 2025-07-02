# import the librareies
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.showdata, name='inputname'),
]
