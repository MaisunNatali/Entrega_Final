# Generated by Django 4.1 on 2022-09-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCasa', '0006_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post_imagen'),
        ),
    ]
