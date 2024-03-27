# Generated by Django 3.2.16 on 2024-03-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20240315_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'Объект "обёртка"', 'verbose_name_plural': 'Обёртки'},
        ),
        migrations.AddField(
            model_name='icecream',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Позиция для сортировки'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='category',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Позиция для сортировки'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]