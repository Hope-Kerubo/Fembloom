# Generated by Django 5.1.3 on 2024-12-13 08:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FemBloomApp', '0013_sponsorevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorevent',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sponsorevent',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FemBloomApp.event'),
        ),
    ]