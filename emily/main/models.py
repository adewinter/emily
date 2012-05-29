from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    file = models.ImageField(upload_to="uploaded_images")
    name = models.CharField(max_length=200, null=True, blank=True)