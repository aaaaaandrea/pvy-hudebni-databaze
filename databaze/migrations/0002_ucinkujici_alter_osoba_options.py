# Generated by Django 4.0.3 on 2022-04-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaze', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ucinkujici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat', models.IntegerField(max_length=6, verbose_name='Plat')),
            ],
        ),
        migrations.AlterModelOptions(
            name='osoba',
            options={'verbose_name': ('Osoba',), 'verbose_name_plural': 'Osoby'},
        ),
    ]
