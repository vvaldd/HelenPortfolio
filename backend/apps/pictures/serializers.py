from rest_framework.serializers import ModelSerializer, ChoiceField

from .models import PictureModel


class PictureSerializer(ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ('id', 'title', 'image',)


class PictureDetailsSerializer(ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ('id', 'title', 'album', 'image', 'created_at', 'updated_at',)
