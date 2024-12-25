# Generated by Django 5.1.4 on 2024-12-23 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_app', '0003_alter_post_image_alter_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]