# Generated by Django 4.1 on 2023-06-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_order_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
