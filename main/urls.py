from django.urls import path
from .views import PublicationDetailView, PublicationsListView, CreatePublicationView, UpdatePublicationView, \
 DeletePublicationView, PublicationViewSet

# urlpatterns = [
#     path('publications/', PublicationsListView.as_view()),
#     path('publications/<int:pk>/', PublicationDetailView.as_view()),
#     path('publications/create/', CreatePublicationView.as_view()),
#     path('publications/update/<int:pk>/', UpdatePublicationView.as_view()),
#     path('publications/delete/<int:pk>/', DeletePublicationView.as_view())
# ]

# urlpatterns = [
#     path('publications/', PublicationViewSet.as_view({'get': 'list'})),
#     path('publications/<int:pk>/', PublicationViewSet.as_view({'get': 'retrieve'})),
#     path('publications/create/', PublicationViewSet.as_view({'get': 'create'})),
#     path('publications/update/<int:pk>/', PublicationViewSet.as_view({'get': 'update', 'patch': 'partial_update'})),
#     path('publications/delete/<int:pk>/', PublicationViewSet.as_view({'delete': 'destroy'})),
# ]


urlpatterns = [
    path('publications/', PublicationViewSet.as_view({'get': 'list',
                                                      'post': 'create'})),
    path('publications/<int:pk>/', PublicationViewSet.as_view({'get': 'retrieve',
                                                               'put': 'update',
                                                               'patch': 'partial_update',
                                                               'delete': 'destroy'})),
]