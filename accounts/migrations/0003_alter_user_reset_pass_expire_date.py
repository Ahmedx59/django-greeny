# Generated by Django 5.1 on 2024-09-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_reset_pass_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reset_pass_expire_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]