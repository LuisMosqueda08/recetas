"""
URL configuration for recetas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from recetas_app.views import home_views, user_views, recetas_view

urlpatterns = [
    path('', home_views.home, name='home'),
    path('contacto/', home_views.contacto, name='contacto'),
    path('registro/', user_views.registro, name='registro'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('admin/', admin.site.urls),
    path('receta/<slug:slug>/', recetas_view.receta, name='receta'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

