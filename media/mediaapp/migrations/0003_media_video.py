# Generated by Django 5.1.1 on 2024-10-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaapp', '0002_alter_media_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='video',
            field=models.FileField(default=1, upload_to='video'),
            preserve_default=False,
        ),
    ]
