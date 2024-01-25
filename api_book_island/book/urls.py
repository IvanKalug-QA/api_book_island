from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BookViewSet, PagesViewSet
router = SimpleRouter()
router.register('books', BookViewSet)
router.register(r'books/(?P<book_id>\d+)/pages',
                PagesViewSet, basename='pages')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
