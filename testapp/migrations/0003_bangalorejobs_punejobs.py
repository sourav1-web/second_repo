# Generated by Django 4.2.7 on 2023-11-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_rename_jobs_hydjobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='BangaloreJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('role', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('phno', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PuneJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('role', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('phno', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
            ],
        ),
    ]
