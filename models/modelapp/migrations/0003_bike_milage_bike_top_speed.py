# Generated by Django 5.1.1 on 2024-10-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0002_bike'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='milage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bike',
            name='top_speed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
