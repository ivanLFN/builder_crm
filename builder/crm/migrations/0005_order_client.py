# Generated by Django 4.1 on 2023-06-17 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_imagedb_owner_alter_order_assingned_crew_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='crm.clientcompany'),
        ),
    ]
