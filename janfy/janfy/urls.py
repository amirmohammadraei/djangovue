from django.contrib import admin
from django.urls import path
from conct import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.call_api),
    path('j/', views.index),
]
