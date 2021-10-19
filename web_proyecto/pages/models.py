from django.db import models
from ckeditor.fields import RichTextField

class Video(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    link = models.URLField(verbose_name="Link video")
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Categoria(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    video = models.ManyToManyField(Video)
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    categoria = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name = "universidad"
        verbose_name_plural = "universidades"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


