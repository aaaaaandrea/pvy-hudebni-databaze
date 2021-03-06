# Generated by Django 4.0.5 on 2022-06-04 11:54

import databaze.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaze', '0012_song_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='album',
            new_name='umelec',
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, upload_to=databaze.models.cover_path, verbose_name='Cover'),
        ),
    ]
