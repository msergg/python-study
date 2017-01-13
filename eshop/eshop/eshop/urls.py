"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.list import ListView
from products.views import index
from accounts.views import logout_,login_

from products.models import Product

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list/$', ListView.as_view(model=Product, paginate_by=2), name='list'),
    url(r'^logout/$', logout_, name='logout'),
    url(r'^login/$', login_, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),


]
