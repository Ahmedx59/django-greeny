# Generated by Django 5.1 on 2024-10-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_cart_total_after_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
