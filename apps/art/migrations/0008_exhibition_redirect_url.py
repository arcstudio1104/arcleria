# Generated by Django 2.1.5 on 2020-03-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0007_picture_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='redirect_url',
            field=models.URLField(default='', verbose_name='클릭시 이동'),
        ),
    ]
