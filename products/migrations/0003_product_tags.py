# Generated by Django 5.1 on 2024-09-03 14:54

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_img'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]