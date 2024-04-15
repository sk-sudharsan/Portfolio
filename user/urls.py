from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view/', views.viewcv, name="viewcv"),
    path('download/', views.download_resume, name='download_resume'),
]