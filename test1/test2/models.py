from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
# from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=50, default='')
    content = RichTextUploadingField(blank=True, max_length=300)