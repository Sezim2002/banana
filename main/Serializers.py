from rest_framework import serializers

from main.models import Publication
from main.models import Comment


class PublicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'title', 'text', 'user')


class PublicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep



class CreatePublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'




