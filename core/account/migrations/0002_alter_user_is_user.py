# Generated by Django 4.2.7 on 2024-01-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=True, verbose_name='Is user'),
        ),
    ]
