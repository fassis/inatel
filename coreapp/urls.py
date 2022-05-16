from django.urls import path

from coreapp import views

app_name = 'coreapp'

urlpatterns = [
    path('ubs/import/', 
        views.health_unities_import,
         name='health_unities_import'),
    path('ubs/file/list/', 
        views.health_unity_file_list, 
        name='health_unity_file_list'),
    path('ubs/file/detail/<int:health_unity_file_pk>/',
         views.health_unity_file_detail, 
        name='health_unity_file_detail'),
    path('ubs/file/list/<int:health_unity_file_pk>/',
         views.health_unity_list, 
        name='health_unity_list'),
    path('ubs/list/<slug:state>/',
         views.health_unity_state_list, 
        name='health_unity_state_list')
]