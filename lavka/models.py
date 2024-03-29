from django.db import models
from django.urls import reverse


class ReklavkaCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lavka:category', kwargs={'cat_id': self.pk})


class Reklavka(models.Model):
    title = models.CharField(max_length=255)
    descript = models.TextField()
    photo = models.ImageField(upload_to='static/images', blank=True, verbose_name='Фото')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    cat = models.ForeignKey(ReklavkaCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('lavka:post', kwargs={'post_slug': self.slug})
