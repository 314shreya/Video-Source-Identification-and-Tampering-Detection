from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prnu_main',views.prnu_main, name='prnu_main'),
    path('prnu1', views.prnu1, name='prnu1'),
    path('prnu2', views.prnu2, name='prnu2'),
    path('prnu11', views.prnu11, name='prnu11'),
    path('prnu22', views.prnu22, name='prnu22'),
    path('prnu222', views.prnu222, name='prnu222'),
    path('tamp_main', views.tamp_main, name='tamp_main'),
    path('tamp1', views.tamp1, name='tamp1'),
    # path('findprnu', views.findprnu, name='findprnu')
]
