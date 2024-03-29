# Generated by Django 2.0.9 on 2020-07-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200718_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='school_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='cross1',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cross2',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hack1',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hack2',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hack3',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hack4',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hard1',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hard2',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='prog1',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='prog2',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='prog3',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='quiz1',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='quiz2',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='surp1',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='profile',
            name='surp2',
            field=models.CharField(max_length=30, null=True, verbose_name='Student'),
        ),
    ]
