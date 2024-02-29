from django.db import models


class PicturesModel(models.Model):
    class Meta:
        db_table = 'pictures'

    name = models.CharField(max_length=30)
    format = models.CharField(max_length=10)
    genre = models.CharField(max_length=50)
    mood = models.CharField(max_length=50)
    file = models.ImageField(upload_to='pictures_folder')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
