import uuid

from django.db import models

from .choices import GENRE_CHOICES


class PictureModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    format = models.CharField(max_length=10)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    picture = models.ImageField(upload_to='pictures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title

    class Meta:
        db_table = 'pictures'
