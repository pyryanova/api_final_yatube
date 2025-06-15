from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comment-list'
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view(
            {
                'get': 'retrieve',
                'patch': 'partial_update',
                'put': 'update',
                'delete': 'destroy'
            }
        ),
        name='comment-detail'
    ),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
