# Generated by Django 3.0.7 on 2022-06-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('Roll_number', models.IntegerField()),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
