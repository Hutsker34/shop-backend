# Generated by Django 4.2 on 2023-04-29 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend_api.order', verbose_name='заказ')),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend_api.product', verbose_name='продукт')),
            ],
        ),
    ]
