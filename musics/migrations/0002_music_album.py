# Generated by Django 4.1.3 on 2022-11-04 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]