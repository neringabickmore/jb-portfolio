# Generated by Django 3.2 on 2021-05-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0004_auto_20210515_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Celebrities Section',
            },
        ),
        migrations.CreateModel(
            name='Commercials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Commercials Section',
            },
        ),
        migrations.CreateModel(
            name='Editorials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Editorials Section',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Music Section',
            },
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'TV Section',
            },
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='assisted',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
