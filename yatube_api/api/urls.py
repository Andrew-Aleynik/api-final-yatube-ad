from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"groups", GroupViewSet, basename="group")
router.register(r"follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
    path(
        "posts/<int:post_id>/comments/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="post-comments-list",
    ),
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        CommentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="post-comments-detail",
    ),
]
