# Generated by Django 5.1 on 2024-10-10 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_coupon_order_total_after_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='oeder_time',
            new_name='order_time',
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_coupon', to='orders.coupon'),
        ),
    ]
