# Generated by Django 4.2.5 on 2023-12-11 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0025_alter_post_hashtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]
