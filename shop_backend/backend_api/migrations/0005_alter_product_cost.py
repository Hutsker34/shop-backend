# Generated by Django 4.2 on 2023-04-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_remove_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.CharField(max_length=100),
        ),
    ]
