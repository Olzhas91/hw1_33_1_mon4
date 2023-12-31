# Generated by Django 4.2.6 on 2023-10-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Название принтера')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Загрузите фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Дайте описание')),
                ('type_printer', models.CharField(choices=[('МФУ', 'МФУ'), ('Лазерный', 'Лазерный'), ('Цветной', 'Цветной'), ('Фентези', 'Фентези')], max_length=100, null=True, verbose_name='выебрите модель')),
                ('cost', models.PositiveIntegerField(null=True, verbose_name='Укажите цену')),
                ('date_start', models.DateField(null=True, verbose_name='Укажите дату изготовления')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
