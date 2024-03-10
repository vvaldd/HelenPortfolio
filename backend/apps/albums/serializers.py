from rest_framework.serializers import ModelSerializer

from apps.albums.models import AlbumModel
from apps.pictures.serializers import PictureSerializer


class AlbumSerializer(ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = AlbumModel
        fields = ('id', 'album', 'pictures')
