# Generated by Django 2.1.2 on 2018-11-06 05:11

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20181106_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='url_endpoint',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='short_name'),
        ),
    ]
