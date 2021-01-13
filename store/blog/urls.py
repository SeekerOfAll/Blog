from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .api import PostViewSet, CategoryViewSet, CommentViewSet
from .views import CategoryArchive, like_comment, CategoryDetail, PostArchive, \
    PostDetail, create_comment
from store.urls import router
# router = DefaultRouter()
# post_list_view = PostViewSet.as_view({'get': 'list', 'post': 'create'})
# post_detail_view = PostViewSet.as_view(
#     {'get': 'retrieve', 'post': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    # path('', home, name='posts_archive'),
    path('', PostArchive.as_view(), name='posts_archive'),  # class base view

    # path('posts/<slug:pk>/', post_single, name='post_single'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post_single'),  # class base view

    # path('categories/', categories_archive, name='categories_archive'),
    path('categories/', CategoryArchive.as_view(), name='categories_archive'),  # class base view

    # path('categories/<slug:pk>/', category_single, name='category_single'),
    path('categories/<slug:slug>/', CategoryDetail.as_view(), name='category_single'),  # class base view

    path('like_comment/', like_comment, name='like_comment'),
    path('comments/', create_comment, name='add_comment'),
    # path('api/posts/', post_list_view, name='post_list'),
    # path('api/posts/<int:pk>/', post_detail_view, name='post_detail'),
    # path('api/comments/', comment_list, name='comment_list'),
    # path('api/comments/<int:pk>/', comment_detail, name='comment_detail'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
