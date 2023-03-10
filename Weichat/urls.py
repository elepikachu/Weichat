"""Weichat URL Configuration

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

from . import views
from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('help', views.help_view),
    path('register', views.register_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('chooce', views.choose_view),
    path('upload', views.upload_view),
    path('chat/', include('chat.urls')),
    path('robots.txt', views.robots_txt),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
