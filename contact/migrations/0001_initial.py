# Generated by Django 5.1 on 2024-08-22 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=400)),
            ],
        ),
    ]
