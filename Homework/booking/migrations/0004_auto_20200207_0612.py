# Generated by Django 3.0.2 on 2020-02-07 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20200207_0612'),
        ('booking', '0003_auto_20200207_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='cleaner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Cleaner'),
        ),
    ]