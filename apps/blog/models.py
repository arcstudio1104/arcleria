from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class Faq(models.Model):
    category = models.CharField('카테고리', max_length=100)
    title = models.CharField('제목', max_length=200)
    content = RichTextUploadingField('내용')
    created = models.DateTimeField('생성일', auto_now_add=True)
    order = models.PositiveIntegerField('순서', default=0)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
        ordering = ['order']

    def get_absolute_url(self):
        return reverse("faq_detail", kwargs={'pk': self.pk})


class Flatpage(models.Model):
    terms = RichTextUploadingField('이용약관')
    privacy = RichTextUploadingField('개인정보처리방침')

    class Meta:
        verbose_name = "이용약관/개인정보처리방침"
        verbose_name_plural = "이용약관/개인정보처리방침"


class BannerHome(models.Model):
    image = models.ImageField("배너 이미지", upload_to='banner/home/')
    image_m = models.ImageField("배너 이미지 (모바일)", upload_to='banner/home/')
    redirect_url = models.URLField("클릭시 이동", default="")

    class Meta:
        verbose_name = "배너(홈)"
        verbose_name_plural = "배너(홈)"


class BannerGallery(models.Model):
    image = models.ImageField("배너 이미지", upload_to='banner/gallery/')
    image_m = models.ImageField("배너 이미지 (모바일)", upload_to='banner/gallery/')
    name = models.CharField("갤러리명", max_length=100)
    place = models.CharField("장소", max_length=100)
    exhibition = models.CharField("전시명", max_length=100)
    date = models.CharField("기간", max_length=100)
    redirect_url = models.URLField("클릭시 이동", default="")

    class Meta:
        verbose_name = "배너(갤러리)"
        verbose_name_plural = "배너(갤러리)"