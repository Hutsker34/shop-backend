# Generated by Django 4.2 on 2023-04-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0008_productinorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='backend_api.ProductInOrder', to='backend_api.product', verbose_name='Товары'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]