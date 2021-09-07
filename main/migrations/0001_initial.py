# Generated by Django 3.2.7 on 2021-09-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    #依存するマイグレーションファイル
    dependencies = [
    ]
    #マイグレーションによる操作
    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBNコード')),
                ('title', models.CharField(max_length=100, verbose_name='書名')),
                ('price', models.IntegerField(default=0, verbose_name='価格')),
                ('publisher', models.CharField(choices=[('PHP出版社', 'PHP出版社'), ('集英社', '集英社'), ('講談社', '講談社'), ('学研', '学研'), ('日経BP社', '日経BP社')], max_length=50, verbose_name='出版社')),
                ('published', models.DateField(verbose_name='刊行日')),
            ],
        ),
    ]