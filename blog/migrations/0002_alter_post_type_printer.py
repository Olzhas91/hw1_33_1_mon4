# Generated by Django 4.2.6 on 2023-10-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type_printer',
            field=models.CharField(choices=[('МФУ', 'МФУ'), ('Лазерный', 'Лазерный'), ('Цветной', 'Цветной')], max_length=100, null=True, verbose_name='выебрите модель'),
        ),
    ]