# Generated by Django 4.0.5 on 2022-10-26 07:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_picture', models.ImageField(default='blog_masonry_01.jpg', upload_to='profile_images')),
                ('news_title', models.CharField(blank=True, max_length=50)),
                ('news_preview_body', models.TextField(blank=True)),
                ('news_main_body', models.TextField(blank=True)),
                ('news_date', models.DateTimeField(default=datetime.datetime.now)),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.category')),
                ('news_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
