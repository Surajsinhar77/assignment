# urls.py (of your app)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentCreateAPIView, CommentListAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentCreateAPIView, CommentListAPIView
from .views import UserCreateAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', include(router.urls)),
    path('api/users/', UserCreateAPIView.as_view(), name='user-create'),
    path('posts/<int:post_pk>/comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('posts/<int:post_pk>/comments/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]