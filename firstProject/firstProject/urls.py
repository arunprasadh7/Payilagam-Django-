"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to dv. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from firstApp import views
from demoApp import views as dv
# from timeapp import views as tv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.wish),
    path('gm/',dv.gm_view),
    path('ga/',dv.ga_view),
    path('ge/',dv.ge_view),
    path('timeapp/',include('timeapp.urls')),
    path('demoTemplate/',include('demoTemplate.urls')),
]

