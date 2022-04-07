from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_color', views.update_color, name='update_color'),
    path('update_data', views.update_data, name='update_data'),
    path('data_table', views.data_table, name='data_table'),
]
