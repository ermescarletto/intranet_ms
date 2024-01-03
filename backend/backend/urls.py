"""backend URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("users/", include("users.urls"), name='users'),
    #path("", auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path("",include("intranet.urls"), name="intranet"),
    path("cadastros/",include("cadastros.urls"), name='cadastros'),
    path("cms/", include("cms.urls"), name='cms'),
    #path("crm/", include("crm.urls"), name='crm'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
