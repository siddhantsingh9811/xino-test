# Generated by Django 2.0.9 on 2020-07-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200723_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='prog3',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
    ]
