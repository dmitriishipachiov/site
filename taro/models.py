from django.db import models
from django.urls import reverse



class Arkan(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField()
    photo = models.ImageField(verbose_name='Фото')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
