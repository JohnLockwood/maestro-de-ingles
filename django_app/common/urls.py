from django.urls import path

from . import views

app_name = 'common'  # Namespaces the views

urlpatterns = [
    path('', views.index, name='index')
]