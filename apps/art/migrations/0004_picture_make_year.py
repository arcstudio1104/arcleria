# Generated by Django 2.1.5 on 2020-02-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_exhibition_is_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='make_year',
            field=models.CharField(default='', max_length=30, verbose_name='제작년도'),
        ),
    ]