"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first),
    path('reg',views.reg),
    path('addreg',views.addreg),
    path('login',views.login),
    path('logreg',views.logreg),
    path('profile/', views.profile, name='profile'),
    path('logout',views.logout),
    path('viewuser',views.viewuser),
    path('profile',views.profile),
    path('update/<int:id>',views.update),
    path('deleteuser/<int:id>',views.deleteuser),
    path('update/addupdate/<int:id>',views.addupdate),
    path('admin/', admin.site.urls),
]

