from django.db import models

# Create your models here.
class Book(models.Model):
    #フィールド情報を定義
    isbn = models.CharField(
        verbose_name='ISBNコード',
        max_length=20
    )

    title = models.CharField(
        verbose_name='書名',
        max_length=100
    )

    price = models.IntegerField(
        verbose_name='価格',
        default=0
    )

    publisher = models.CharField(
        verbose_name='出版社',
        max_length=50,
        choices=[
            ('PHP出版社','PHP出版社'),
            ('集英社','集英社'),
            ('講談社','講談社'),
            ('学研','学研'),
            ('日経BP社','日経BP社')
        ],
    )

    published = models.DateField(
        verbose_name='刊行日'
    )

    #モデルの文字列表現
    def __str__(self):
        return f'{self.title}({self.publisher}/{self.price}円)'