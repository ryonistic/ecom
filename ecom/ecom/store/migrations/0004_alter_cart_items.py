# Generated by Django 3.2.13 on 2022-05-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='store.Product'),
        ),
    ]
