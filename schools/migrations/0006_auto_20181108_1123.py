# Generated by Django 2.1.2 on 2018-11-08 05:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_school_abc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='abc',
            field=tinymce.models.HTMLField(),
        ),
    ]
