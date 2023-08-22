from django.db import models

class GalleryItem(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField()

    def __str__(self):
        return self.title