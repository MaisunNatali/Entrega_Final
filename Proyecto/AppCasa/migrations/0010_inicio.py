# Generated by Django 4.1 on 2022-09-24 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCasa', '0009_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='inicio')),
            ],
        ),
    ]
