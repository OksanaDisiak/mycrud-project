# Generated by Django 4.0 on 2022-01-07 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=250)),
                ('second_name', models.CharField(max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('make', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('plate_number', models.CharField(max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycrudApp.driver')),
            ],
        ),
    ]
