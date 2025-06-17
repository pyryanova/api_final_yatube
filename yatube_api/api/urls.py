from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'follow', FollowViewSet, basename='follow')

# хотела сделать с NestedDefaultRouter, но у Практикума падают тесты,
# а было красиво..

# from rest_framework_nested.routers import NestedDefaultRouter
# posts_router = NestedDefaultRouter(router, r'posts', lookup='post')
# posts_router.register(r'comments', CommentViewSet, basename='post-comments')

router.register(
    r'posts/(?P<post_pk>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/', include(posts_router.urls)),  # отключено
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
