from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
# from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
# from rest_framework.response import Response
#
# from main.Serializers import PublicationListSerializer, PublicationDetailSerializer
# from main.models import Publication
#
#
# # @api_view(['GET'])
# # def test_view(request):
# #     return Response('Hello world')
#
#
# class PublicationsListCreatView(ListCreateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationListSerializer
#
#
# class PublicationDetailView(RetrieveUpdateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationDetailSerializer





#
#
#
# # CREAT, LIST, RETRIEVE, UPDATE/PARTIAL_UPDATE, DESTROY
# # POST,           GET,     PUT/PATCH,  DELETE
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.Serializers import PublicationListSerializer, PublicationDetailSerializer, CreatePublicationSerializer
from main.models import Publication

# # НА ФУНКЦИЯХ
# @api_view(['GET'])
# def publications(request):
#     pubs = Publication.objects.all()   # -  список объявлений
#     serializer = PublicationListSerializer(pubs, many=True)
#     # - словарь {id: ..., title:..., text:...} -> переводит ф фронтенд формат
#     return Response(serializer.data)  # - возвращает ответ(HTTP)
#
#
# #НА КЛАССАХ(1)
# class PublicationListView(APIView):
#     def get(self, request):
#         pubs = Publication.objects.all()
#         serializer = PublicationListSerializer(pubs, many=True)
#         return Response(serializer.data)
#
#
# #НА КЛАССАХ(2)
class PublicationsListView(ListAPIView):
    queryset = Publication.objects.all() # - хранится список
    serializer_class = PublicationListSerializer

# APIView - get
# ListAPIView - get
# CreateAPIView - post


class PublicationDetailView(RetrieveAPIView): #-детали(всю информацию одной публикации)
    queryset = Publication.objects.all()
    serializer_class = PublicationDetailSerializer


class CreatePublicationView(CreateAPIView): #-создание
    queryset = Publication.objects.all()
    serializer_class = CreatePublicationSerializer


class UpdatePublicationView(UpdateAPIView):
    queryset = Publication.objects.all()
    serializer_class = CreatePublicationSerializer


class DeletePublicationView(DestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = CreatePublicationSerializer







class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = CreatePublicationSerializer

    def get_serializer_class(self):
        if self.action =='list':
            return PublicationListSerializer
        elif self.action == 'retrieve':
            return PublicationDetailSerializer
        return CreatePublicationSerializer








