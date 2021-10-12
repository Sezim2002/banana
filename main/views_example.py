from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from main.Serializers import PublicationListSerializer, PublicationDetailSerializer
from main.models import Publication
#
#
@api_view(['GET'])
def test_view(request):
    return Response('Hello world')


class PublicationsListCreatView(ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationListSerializer


class PublicationDetailView(RetrieveUpdateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationDetailSerializer


# # CREATE, LIST, RETRIEVE, UPDATE/PARTIAL_UPDATE, DESTROY
# # POST,           GET,     PUT/PATCH,  DELETE
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.Serializers import PublicationListSerializer, PublicationDetailSerializer, CreatePublicationSerializer, \
    CommentSerializer
from main.models import Publication, Comment
#
# # НА ФУНКЦИЯХ
from main.permissions import IsAuthorOrIsAdmin, IsAuthor
#
#
@api_view(['GET'])
def publications(request):
    pubs = Publication.objects.all()   # -  список объявлений
    serializer = PublicationListSerializer(pubs, many=True)
    # - словарь {id: ..., title:..., text:...} -> переводит ф фронтенд формат
    return Response(serializer.data)  # - возвращает ответ(HTTP)

# #
# # # НА КЛАССАХ(1)
# class PublicationListView(APIView):
#     def get(self, request):
#         pubs = Publication.objects.all()
#         serializer = PublicationListSerializer(pubs, many=True)
#         return Response(serializer.data)
#
#
# # НА КЛАССАХ(2)
# class PublicationsListView(ListAPIView):
#     queryset = Publication.objects.all() # - хранится список
#     serializer_class = PublicationListSerializer
#
# # APIView - get
# # ListAPIView - get
# # CreateAPIView - post
#
#
# class PublicationDetailView(RetrieveAPIView):  # детали(всю информацию одной публикации)
#     queryset = Publication.objects.all()
#     serializer_class = PublicationDetailSerializer
#
#
# class CreatePublicationView(CreateAPIView):  # создание
#     queryset = Publication.objects.all()
#     serializer_class = CreatePublicationSerializer
#
#
# class UpdatePublicationView(UpdateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = CreatePublicationSerializer
#
#
# class DeletePublicationView(DestroyAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = CreatePublicationSerializer


# TODO: Объявления создаются со статусом draft, а затем автор может поменять на open
# TODO: черновик не отображается в общем списке - его может видет только автор
class PublicationViewSet(viewsets.ModelViewSet):
    # список объектов модели
    queryset = Publication.objects.all()
    # класс, которым будут сериализоваться эти объекты
    serializer_class = CreatePublicationSerializer
    # проверяет права для действия с объектами через APIView
    permission_classes = [IsAuthorOrIsAdmin]
    # pagination_class = класс пагинации для данной вьюшки
    # paginate_by = page_size для данной вьюшки

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == ['update', 'partial_update', 'destroy']:
            return [IsAuthorOrIsAdmin]
        return []

    def get_serializer_class(self):
        if self.action == 'list':
            return PublicationListSerializer
        elif self.action == 'retrieve':
            return PublicationDetailSerializer
        return CreatePublicationSerializer

    # фильтрация
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     request = self.request
    #     status = request.query_params.get('status')
    #      if status is not None:
    #        queryset = queryset.filter(status=status)
    #     return queryset


# http://127.0.0.1:8000/publications/?status=closed&created_at=...


# TODO: сделать комментарии,создавать комментарии может только залогиненный пользователь,
#  редактировать и удалять только автор
# TODO: пагинация, фильтрация, поиск

class CreateCommentsView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}


class UpdateCommentView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]


class DeleteCommentView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]



from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CommentViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor]

