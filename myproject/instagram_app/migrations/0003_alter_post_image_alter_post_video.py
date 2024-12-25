# Generated by Django 5.1.4 on 2024-12-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_app', '0002_post_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='post_video/'),
        ),
    ]
