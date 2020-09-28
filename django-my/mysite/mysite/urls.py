"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blog import views
from django.conf.urls import url
from credit import views as credit_views

extra_patterns = [
    path('reports', credit_views.report),
    path('reports/<int:id>', credit_views.report),
    path('charge/', credit_views.charge),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.hello),
    path('credit/', include(extra_patterns)),
]

# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.page_error