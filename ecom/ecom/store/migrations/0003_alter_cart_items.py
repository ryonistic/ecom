# Generated by Django 3.2.13 on 2022-05-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='store.Product'),
        ),
    ]