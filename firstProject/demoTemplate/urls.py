from django.contrib import admin
from django.urls import path
from demoTemplate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',views.display)
]