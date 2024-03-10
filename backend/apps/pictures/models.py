import uuid

from django.db import models

from apps.albums.models import AlbumModel


class PictureModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30, unique=True)
    album = models.ForeignKey(AlbumModel, on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(upload_to='pictures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pictures'
