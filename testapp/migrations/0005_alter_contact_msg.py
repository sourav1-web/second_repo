# Generated by Django 4.2.7 on 2024-01-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(max_length=120),
        ),
    ]
