# Generated by Django 4.2 on 2023-07-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0016_product_tupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tupe',
            field=models.CharField(choices=[('cap', 'кепка'), ('jamper', 'свитер'), ('T-shirt', 'футболка'), ('glass', 'очки'), ('skirt', 'юбка'), ('pants', 'штаны'), ('default', 'другое')], default='default', max_length=100),
        ),
    ]