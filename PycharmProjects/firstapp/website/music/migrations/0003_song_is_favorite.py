# Generated by Django 3.0.2 on 2020-01-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200128_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]