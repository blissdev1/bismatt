"""
URL configuration for Bismatt project.

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
from django.contrib import admin
from django.urls import include, path
from Bismatt import settings
from django.conf.urls.static import static
from Cars.views import home_view, car_view, ecar_view, json_view, create_user_view, login_view, search_view, contact_view, about_view

urlpatterns = [
    path("", home_view, name="home"),
    path("cars/", car_view, name="cars"),
    path("cars/<str:pk>/", ecar_view, name="ecar"),
    path("json/", json_view, name="json"),
    path("login/", login_view, name="login"),
    path("createuser/", create_user_view, name="createuser"),
    path("search/", search_view, name="search"),
    path("contact/", contact_view, name="contact"),
    path("about/", about_view, name="about"),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
