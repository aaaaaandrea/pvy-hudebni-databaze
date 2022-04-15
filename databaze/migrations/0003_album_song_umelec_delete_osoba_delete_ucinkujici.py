# Generated by Django 4.0.3 on 2022-04-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaze', '0002_ucinkujici_alter_osoba_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_album', models.CharField(max_length=100, verbose_name='Název')),
                ('datum_vydani', models.DateField(blank=True, null=True, verbose_name='Datum vydání')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_song', models.CharField(max_length=100, verbose_name='Název')),
                ('datum_vydani', models.DateField(blank=True, null=True, verbose_name='Datum vydání')),
            ],
            options={
                'verbose_name': ('Song',),
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.CreateModel(
            name='umelec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100, verbose_name='Jméno')),
                ('datum_zalozeni', models.DateField(blank=True, null=True, verbose_name='Datum vzniku')),
            ],
        ),
        migrations.DeleteModel(
            name='Osoba',
        ),
        migrations.DeleteModel(
            name='Ucinkujici',
        ),
    ]
