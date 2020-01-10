"""learn_django_with_maybejay URL Configuration

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
from pages import views
import firstapp.views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', fv.product_details_view, name='home'),
    path('details/', fv.product_details_view, name='home'),
    path('', fv.product_details_view, name='home'),
    path('products/', fv.product_details_view),
    path('create/', fv.product_create_view),
    path('products/<int:product_id>/', fv.dynamic_lookup_view, name='product')
]
