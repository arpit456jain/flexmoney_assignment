# Generated by Django 3.2.16 on 2022-12-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alredy_registered_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('payment_month', models.CharField(max_length=150)),
                ('payment_year', models.CharField(max_length=150)),
                ('batch_time', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Application_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=150)),
                ('payment_month', models.CharField(max_length=150)),
                ('payment_year', models.CharField(max_length=150)),
                ('batch_time', models.CharField(max_length=150)),
            ],
        ),
    ]
