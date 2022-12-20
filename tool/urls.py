from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('csv_home',views.csv_home,name='csv_home'),
    path('pdf_home',views.pdf_home,name='pdf_home')
]