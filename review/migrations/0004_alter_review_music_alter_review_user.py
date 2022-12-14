# Generated by Django 4.1.3 on 2022-11-14 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0006_alter_music_likes_alter_music_music_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0003_review_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='music',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_set', to='musics.music'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
