# Generated by Django 4.1 on 2023-06-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcompany',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='country',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='house',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='region',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientcompany',
            name='street',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]