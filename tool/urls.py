from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('drive_home',views.drive_home,name='drive_home'),
    
    #common
    path('create/<str:file_type>',views.create,name='create'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('hive_edit/<int:id>/',views.hive_edit,name='hive_edit'),

    #csv
    path('csv_home',views.csv_home,name='csv_home'),

    #pdf
    path('pdf_home',views.pdf_home,name='pdf_home')

]