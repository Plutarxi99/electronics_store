# Generated by Django 5.0.2 on 2024-02-21 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта звена сети')),
                ('country', models.CharField(blank=True, max_length=120, null=True, verbose_name='Страна нахождения звена сети')),
                ('city', models.CharField(blank=True, max_length=120, null=True, verbose_name='Город нахождения звена сети')),
                ('street', models.CharField(blank=True, max_length=120, null=True, verbose_name='Улица нахождения звена сети')),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер дома звена сети')),
            ],
            options={
                'verbose_name': 'Контакт звена сети',
                'verbose_name_plural': 'Контакты звена сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Названия продукта произведенного звеном сети')),
                ('type', models.CharField(blank=True, max_length=120, null=True, verbose_name='Модель продукта произведенного звеном сети')),
                ('release', models.DateField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт звена сети',
                'verbose_name_plural': 'Продукты звена сети',
            },
        ),
        migrations.CreateModel(
            name='UnionChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название звена сети')),
                ('level_union', models.PositiveSmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='Уровень звена сети')),
                ('level_in_retail', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Уровень звена по отношению к поставщику')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания задолженности')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contact', to='retail.contact', verbose_name='Адрес звена сети')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='retail.product', verbose_name='Продукт произведенный звеном сети')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.unionchain', verbose_name='Поставщик от звена сети')),
            ],
            options={
                'verbose_name': 'Звено сети',
                'verbose_name_plural': 'Звенья сети',
            },
        ),
    ]
