from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import BookViewSet, PagesViewSet, UserViewSet

router = SimpleRouter()
router.register('books', BookViewSet)
router.register(r'books/(?P<book_id>\d+)/pages',
                PagesViewSet, basename='pages')
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-get-token/', views.obtain_auth_token)
]
