"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'^jet/', include('jet.urls', 'jet')),
    path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', Main_Page.as_view(), name='home'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('items/<str:ct_model>/<str:slug>/', Items_Details.as_view(), name='item'),
    path('cart/', Cart_View.as_view(), name='cart'),
    path('add_to_cart/<str:ct_model>/<str:slug>/', Add_To_Cart.as_view(), name='add_to_cart'),
    path('remove_from_cart/<str:ct_model>/<str:slug>/', Delete_From_Cart.as_view(), name='remove_from_cart'),
    path('change_count/<str:ct_model>/<str:slug>/', Change_Count_Items.as_view(), name='change_count'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

