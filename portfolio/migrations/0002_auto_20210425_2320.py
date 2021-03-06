# Generated by Django 3.1.3 on 2021-04-25 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name_plural': 'Photos'},
        ),
        migrations.AddField(
            model_name='photo',
            name='friendly_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Friendly Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
