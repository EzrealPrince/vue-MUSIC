from django.db import models


class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    email = models.EmailField()

class star(models.Model):
    star_name=models.CharField(max_length=30)
    star_sex=models.CharField(max_length=30)
    star_country=models.CharField(max_length=30)
    star_type=models.CharField(max_length=30)
    star_pinyin=models.CharField(max_length=30)

class song(models.Model):
    song_name=models.CharField(max_length=80)
    song_author=models.ForeignKey(star,on_delete=models.DO_NOTHING)
    song_language=models.CharField(max_length=80)
    song_type=models.CharField(max_length=80)
    song_pinyin=models.CharField(max_length=80)
  




# Create your models here.
