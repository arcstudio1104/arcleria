# Generated by Django 2.1.5 on 2020-02-02 06:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='카테고리')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='내용')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('modified', models.DateTimeField(verbose_name='수정일')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='순서')),
            ],
            options={
                'verbose_name': '자주묻는질문',
                'verbose_name_plural': '자주묻는질문',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Flatpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='이용약관')),
                ('privacy', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='개인정보처리방침')),
            ],
            options={
                'verbose_name': '이용약관/개인정보처리방침',
                'verbose_name_plural': '이용약관/개인정보처리방침',
            },
        ),
    ]
