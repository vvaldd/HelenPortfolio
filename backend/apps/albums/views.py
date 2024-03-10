from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.albums.models import AlbumModel
from apps.albums.serializers import AlbumSerializer
from apps.pictures.serializers import PictureSerializer


class AlbumsListCreateView(ListCreateAPIView):
    queryset = AlbumModel.objects.all()
    serializer_class = AlbumSerializer


class AlbumsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AlbumModel.objects.all()
    serializer_class = AlbumSerializer


class AlbumListCreatePicturesView(CreateAPIView):
    queryset = AlbumModel.objects.all()
    serializer_class = PictureSerializer

    def perform_create(self, serializer):
        album = self.get_object()
        serializer.save(album=album)

    def get(self, request, *args, **kwargs):
        album = self.get_object()
        serializer = self.serializer_class(album.pictures, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
