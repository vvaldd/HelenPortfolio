from rest_framework import fields
from rest_framework.serializers import ModelSerializer, ChoiceField

from .choices import GENRE_CHOICES
from .models import PictureModel


class CustomMultipleChoiceField(fields.ChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))


class PictureSerializer(ModelSerializer):
    genre = ChoiceField(choices=GENRE_CHOICES, required=False)

    class Meta:
        model = PictureModel
        fields = ('id', 'title', 'format', 'genre', 'image', 'created_at', 'updated_at',)


class PictureDetailsSerializer(ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ('id', 'title', 'format', 'genre', 'image', 'created_at', 'updated_at',)
