# Generated by Django 2.1.2 on 2018-11-04 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
        ('pages', '0009_auto_20181104_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='prev_school_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev_school_1', to='schools.school'),
        ),
        migrations.AddField(
            model_name='intern',
            name='prev_school_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev_school_2', to='schools.school'),
        ),
    ]
