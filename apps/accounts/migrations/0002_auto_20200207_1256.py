# Generated by Django 2.1.5 on 2020-02-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=10, verbose_name='이름'),
        ),
    ]
