# Generated by Django 2.0.9 on 2020-07-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200723_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cross1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cross2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hack1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hack2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hack3',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hack4',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hard1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hard2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prog1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prog2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prog3',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='quiz1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='quiz2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surp1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surp2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Student'),
        ),
    ]
