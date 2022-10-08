from django.contrib import admin
from django.urls import path

from registry import views
from registry.views import dataTable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('data_table.html/', dataTable)
]
