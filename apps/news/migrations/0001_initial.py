

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Изображение новости')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('author_fullname', models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО автора')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на источник')),

                ('is_favorite', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
