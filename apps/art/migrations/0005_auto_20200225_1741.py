# Generated by Django 2.1.5 on 2020-02-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_picture_make_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='make_year',
            field=models.CharField(max_length=30, verbose_name='제작년도'),
        ),
    ]
