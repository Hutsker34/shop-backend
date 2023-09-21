# Generated by Django 4.2.4 on 2023-09-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0019_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('cap', 'кепка'), ('jamper', 'свитер'), ('tshirt', 'футболка'), ('glass', 'очки'), ('skirt', 'юбка'), ('pants', 'штаны'), ('default', 'другое')], default='default', max_length=100),
        ),
    ]