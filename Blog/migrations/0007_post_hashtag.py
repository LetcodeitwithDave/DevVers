# Generated by Django 4.2.5 on 2023-10-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
