# Generated by Django 2.1.5 on 2020-08-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_faq_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner/gallery/', verbose_name='배너 이미지')),
                ('image_m', models.ImageField(upload_to='banner/gallery/', verbose_name='배너 이미지 (모바일)')),
                ('name', models.CharField(max_length=100, verbose_name='갤러리명')),
                ('place', models.CharField(max_length=100, verbose_name='장소')),
                ('exhibition', models.CharField(max_length=100, verbose_name='전시명')),
                ('date', models.CharField(max_length=100, verbose_name='기간')),
            ],
            options={
                'verbose_name': '배너(갤러리)',
                'verbose_name_plural': '배너(갤러리)',
            },
        ),
        migrations.CreateModel(
            name='BannerHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner/home/', verbose_name='배너 이미지')),
                ('image_m', models.ImageField(upload_to='banner/home/', verbose_name='배너 이미지 (모바일)')),
                ('redirect_url', models.URLField(default='', verbose_name='클릭시 이동')),
            ],
            options={
                'verbose_name': '배너(홈)',
                'verbose_name_plural': '배너(홈)',
            },
        ),
    ]
