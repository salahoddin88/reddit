"""reddit URL Configuration

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
from django.urls import path, include

""" django.conf package is imported to config media URL 
    settings are imported because PROJECTNAME/settings.py file contain MEDIA_URL and MEDIA_ROOT configuration, and we need to add the configuration to PROJECT URL PATTERN.
"""
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    is added to add URL PATTERN for uploaded media to server in browser
"""
