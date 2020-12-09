from django.contrib import admin
from django.urls import path
from janfy.conct import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.call_api)
]
