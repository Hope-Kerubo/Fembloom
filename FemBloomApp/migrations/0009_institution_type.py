# Generated by Django 5.1.3 on 2024-12-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FemBloomApp', '0008_useranswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='type',
            field=models.CharField(choices=[('school', 'School'), ('hospital', 'Hospital')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
