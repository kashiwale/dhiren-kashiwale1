"""dj_pd URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view

from main import urls as main_app_urls
from users import urls as users_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name='home' ),
    path('performance/', include('products.urls', namespace='products')),
    path('upload/', include('csvs.urls', namespace='csvs')),
    path('customers/', include('customers.urls', namespace='customers')),
    path('', include(main_app_urls)),
    path('', include(users_app_urls)),
    # path('main/', include('main.urls', namespace='main')),
    #path('home/', include('main.urls', namespace='main')),
    # path('list/', include('main.urls', namespace='main')),
    # path('listing/<str:id>/', include('main.urls', namespace='main')),
    # path('listing/<str:id>/edit/', include('main.urls', namespace='main')),
    # path('listing/<str:id>/like/', include('main.urls', namespace='main')),
    # path('listing/<str:id>/inquire/',
    #      include('main.urls', namespace='main')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
