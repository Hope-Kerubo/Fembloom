# Generated by Django 5.1.3 on 2024-12-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FemBloomApp', '0004_remove_quiz_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Signup',
        ),
    ]
