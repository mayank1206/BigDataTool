from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('drive_home',views.drive_home,name='drive_home'),
    path('csv_home',views.csv_home,name='csv_home'),
    path('pdf_home',views.pdf_home,name='pdf_home'),
    
    #csv
    path('csv_edit',views.csv_edit,name='csv_edit')
]