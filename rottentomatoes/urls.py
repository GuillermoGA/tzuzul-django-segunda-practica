"""rottentomatoes URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from reviews import views as reviews_views
from movies import views as movies_views
from users import views as users_views
from .views import index

router = routers.SimpleRouter()
router.register(r'reviews', reviews_views.ReviewModelViewSet)
router.register(r'movies', movies_views.MovieModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include((router.urls, 'api'))),
    path('api/login/', users_views.Login.as_view()),
    path('api/logout/', users_views.Logout.as_view()),
    path('api/register/', users_views.CreateUserView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
