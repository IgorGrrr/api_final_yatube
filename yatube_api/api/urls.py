from django.urls import path, include

from rest_framework.routers import  DefaultRouter

from .views import PostViewset, GroupViewset, CommentViewset, FollowViewset


router = DefaultRouter()
router.register('posts', PostViewset, basename='posts')
router.register('groups', GroupViewset, basename='groups')
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewset,
    basename='comments'
)
router.register('follow', FollowViewset, basename='follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
