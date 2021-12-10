from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from categories import views as categories_views
from movies import views as movies_views
from reviews import views as reviews_views
from users import views as users_views
from . import views

router = routers.SimpleRouter()
router.register(r'reviews', reviews_views.ReviewModelViewSet)
router.register(r'movies', movies_views.MovieModelViewSet)


urlpatterns = [
    # Admin Area
    path('admin/', admin.site.urls),

    # Website
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('movies/<int:id>', views.movie_details, name='movie_details'),

    # API
    path('api/', include((router.urls, 'api'))),
    path('api/categories/', categories_views.CategoryListView.as_view()),
    path('api/login/', users_views.Login.as_view(), name="api_login"),
    path('api/logout/', users_views.Logout.as_view(), name="api_logout"),
    path('api/register/', users_views.CreateUserView.as_view(), name="api_register"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
