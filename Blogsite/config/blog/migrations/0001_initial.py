# Generated by Django 4.1.7 on 2023-04-28 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(unique=True, verbose_name='آدرس دسته بندی')),
                ('position', models.IntegerField(verbose_name='جایگاه')),
                ('is_active', models.BooleanField(default=False, verbose_name='نمایش داده شود؟')),
            ],
            options={
                'verbose_name': 'دسته بند ی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['-position'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')),
                ('description', models.TextField(verbose_name='محتوا')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='تصویر مقاله')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت')),
                ('category', models.ManyToManyField(related_name='blogs', to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]