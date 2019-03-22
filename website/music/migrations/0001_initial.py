# Generated by Django 2.1.7 on 2019-03-20 11:49

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('album_logo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=100)),
                ('song_title', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='music.Album')),
            ],
        ),
    ]
