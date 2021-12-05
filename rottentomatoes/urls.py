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
