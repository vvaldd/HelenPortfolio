from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import PictureModel
from .serializers import PictureSerializer, PictureDetailsSerializer


class PicturesListCreateView(ListCreateAPIView):
    queryset = PictureModel.objects.all()
    serializer_class = PictureDetailsSerializer


class PicturesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PictureModel.objects.all()
    serializer_class = PictureDetailsSerializer
