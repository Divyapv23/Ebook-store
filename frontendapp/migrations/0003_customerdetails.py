# Generated by Django 4.2.1 on 2023-07-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('frontendapp', '0002_cartaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Mail', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Confirm', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
