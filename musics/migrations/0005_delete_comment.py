# Generated by Django 4.1.3 on 2022-11-05 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
