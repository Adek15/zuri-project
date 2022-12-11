from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    stage_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.stage_name


class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    genre = models.CharField(max_length=50)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lyrics(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
