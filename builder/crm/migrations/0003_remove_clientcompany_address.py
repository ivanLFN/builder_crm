# Generated by Django 4.1 on 2023-06-17 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_clientcompany_city_alter_clientcompany_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcompany',
            name='address',
        ),
    ]
