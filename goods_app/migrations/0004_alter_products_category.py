# Generated by Django 5.1.1 on 2024-10-15 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_app', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods_app.categories', verbose_name='Категория'),
        ),
    ]
