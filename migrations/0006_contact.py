# Generated by Django 4.0 on 2022-03-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_data_result_from_symp_data_result_from_xray_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField(max_length=30)),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]
