# Generated by Django 4.2.5 on 2023-11-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0015_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, default='images/images.png', null=True, upload_to='images/'),
        ),
    ]
