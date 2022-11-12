# Generated by Django 4.1.2 on 2022-11-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ioc',
            fields=[
                ('ioc', models.TextField(primary_key=True, serialize=False)),
                ('type', models.TextField(choices=[('IP', 'Ip'), ('Hash', 'Hash'), ('Domain', 'Domain'), ('URL', 'Url'), ('File', 'File')])),
                ('sources', models.JSONField()),
                ('frequency', models.IntegerField()),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('location', models.JSONField(null=True)),
            ],
        ),
    ]
