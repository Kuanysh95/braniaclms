from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig


app_name = MainappConfig.name


urlpatterns = [

    path('', views.hello_world, name='hello_world'),
    path('<str:word>/', views.blog),
]