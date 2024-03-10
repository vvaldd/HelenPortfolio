from django.db import models


class AlbumModel(models.Model):
    album = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'albums'

