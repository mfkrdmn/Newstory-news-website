from hashlib import blake2b
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.

writer = get_user_model()

class category(models.Model):
    category_name = models.CharField(max_length=50, blank=True)

    def __str__(self) :
        return self.category_name


class news(models.Model):
    news_picture = models.ImageField(upload_to='news_images', default="blog_masonry_01.jpg")
    news_title = models.CharField(max_length=50, blank=True)
    news_preview_body = models.TextField(blank=True)
    news_main_body = models.TextField(blank=True)
    news_category = models.ForeignKey(category, on_delete=models.CASCADE)
    news_date = models.DateTimeField(default=datetime.now)
    news_writer = models.ForeignKey(writer, on_delete=models.CASCADE)

    def __str__(self) :
        return self.news_title