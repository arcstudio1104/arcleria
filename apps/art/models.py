from django.db import models


PICTURE_BUY_PROCESS = [
    ('입찰 중', '입찰 중'),
    ('판매 중', '판매 중'),
    ('작품 구매 문의', '작품 구매 문의'),
]

PICTURE_KIND = [
    ('회화', '회화'),
    ('추상화', '추상화'),
    ('프린팅', '프린팅'),
    ('드로잉', '드로잉'),
    ('사진', '사진'),
    ('조긱품', '조각품'),
]


class Artist(models.Model):
    name = models.CharField("작가 이름", max_length=50)
    native = models.CharField("작가 출신", max_length=50, blank=True)
    birth_year = models.CharField("태어난 년도", max_length=30, blank=True)
    introduce = models.TextField("작가 소개")
    belong = models.TextField("소속 및 단체", blank=True)
    award = models.TextField("이력", blank=True)
    collection = models.TextField("작품 소장처", blank=True)
    exhibition_history = models.TextField("전시 경력", blank=True)
    like = models.PositiveSmallIntegerField("좋아요", default=0)
    image = models.ImageField("작가 이미지", upload_to='artist/%Y/%m/%d/')
    is_popular = models.BooleanField("인기있는작가", default=False)

    class Meta:
        verbose_name = "작가"
        verbose_name_plural = "작가"

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)

    def is_sale_count(self):
        num = Picture.objects.filter(artist=self, is_sale=True).count()
        return num


class Gallery(models.Model):
    name = models.CharField("갤러리 이름", max_length=100)
    place = models.TextField("장소")
    introduce = models.TextField("갤러리 소개")
    like = models.PositiveSmallIntegerField("좋아요", default=0)
    image_1 = models.ImageField("갤러리 이미지 1", upload_to='gallery/%Y/%m/%d/')
    image_2 = models.ImageField("갤러리 이미지 2", upload_to='gallery/%Y/%m/%d/', blank=True, null=True)
    image_3 = models.ImageField("갤러리 이미지 3", upload_to='gallery/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name = "갤러리"
        verbose_name_plural = "갤러리"

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class Picture(models.Model):
    name = models.CharField("작품명", max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True, related_name='artist_picture')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True, related_name='gallery_picture')
    price = models.CharField("가격", max_length=100)
    make_year = models.CharField("제작년도", max_length=30)
    material = models.CharField("재료", max_length=100)
    kind = models.CharField("종류(유형)", max_length=100, choices=PICTURE_KIND, default="회화")
    size_horizontal = models.PositiveSmallIntegerField("사이즈 가로(cm)", default=0)
    size_vertical = models.PositiveSmallIntegerField("사이즈 세로(cm)", default=0)
    introduce = models.TextField("작품 소개")
    recommend_reason = models.TextField("추천 이유", blank=True)
    is_sale = models.BooleanField("판매 완료", default=False)
    shipping_fee = models.PositiveSmallIntegerField("배송비", default=0)
    buy_process = models.CharField("구매 방식", max_length=20, choices=PICTURE_BUY_PROCESS, default="판매 중")
    like = models.PositiveSmallIntegerField("좋아요", default=0)
    image_1 = models.ImageField("작품 이미지 1", upload_to='picture/%Y/%m/%d/')
    image_2 = models.ImageField("작품 이미지 2", upload_to='picture/%Y/%m/%d/', blank=True, null=True)
    image_3 = models.ImageField("작품 이미지 3", upload_to='picture/%Y/%m/%d/', blank=True, null=True)
    image_4 = models.ImageField("작품 이미지 4", upload_to='picture/%Y/%m/%d/', blank=True, null=True)
    image_5 = models.ImageField("작품 이미지 5", upload_to='picture/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name = "작품"
        verbose_name_plural = "작품"

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class Exhibition(models.Model):
    name = models.CharField("전시명", max_length=100)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True, related_name='gallery_exhibition')
    place = models.CharField("장소", max_length=100)
    date_start = models.DateField("시작일")
    date_end = models.DateField("종료일")
    image_1 = models.ImageField("전시 이미지 1", upload_to='exhibition/%Y/%m/%d/')
    is_end = models.BooleanField("종료", default=False)
    redirect_url = models.URLField("클릭시 이동", default="")

    class Meta:
        verbose_name = "전시"
        verbose_name_plural = "전시"

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class Tag(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_tag')
    tag = models.CharField(max_length=30)

    class Meta:
        verbose_name = "작가 태그"
        verbose_name_plural = "작가 태그"