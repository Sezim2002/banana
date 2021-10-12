from django.urls import path, include
from rest_framework.routers import SimpleRouter

# from .views import PublicationDetailView, PublicationsListView, CreatePublicationView, UpdatePublicationView, \
#     DeletePublicationView, PublicationViewSet, CommentViewSet
# from main.views import (CreateCommentsView, UpdateCommentView, DeleteCommentView, PublicationViewSet, CommentViewSet)
from main.views import PublicationViewSet, CommentViewSet

# 1 способ
# urlpatterns = [
#     path('publications/', PublicationsListView.as_view()),
#     path('publications/<int:pk>/', PublicationDetailView.as_view()),
#     path('publications/create/', CreatePublicationView.as_view()),
#     path('publications/update/<int:pk>/', UpdatePublicationView.as_view()),
#     path('publications/delete/<int:pk>/', DeletePublicationView.as_view())
# ]


# 2 способ
# urlpatterns = [
#     path('publications/', PublicationViewSet.as_view({'get': 'list'})),
#     path('publications/<int:pk>/', PublicationViewSet.as_view({'get': 'retrieve'})),
#     path('publications/create/', PublicationViewSet.as_view({'get': 'create'})),
#     path('publications/update/<int:pk>/', PublicationViewSet.as_view({'get': 'update', 'patch': 'partial_update'})),
#     path('publications/delete/<int:pk>/', PublicationViewSet.as_view({'delete': 'destroy'})),
# ]


# 3 способ
# urlpatterns = [
#     path('publications/', PublicationViewSet.as_view({'get': 'list',
#                                                       'post': 'create'})),
#     path('publications/<int:pk>/', PublicationViewSet.as_view({'get': 'retrieve',
#                                                                'put': 'update',
#                                                                'patch': 'partial_update',
#                                                                'delete': 'destroy'})),
#     path('comments/', CreateCommentsView.as_view()),
#     path('comments/update/<int:pk>/', UpdateCommentView.as_view()),
#     path('comments/delete/<int:pk>/', DeleteCommentView.as_view()),
# ]


# 4 способ
router = SimpleRouter()

router.register('publications', PublicationViewSet, 'publications')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls)),
]