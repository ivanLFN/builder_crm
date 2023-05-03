# Generated by Django 4.2 on 2023-05-03 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0003_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='customuser_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='positions',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_positions', to='users.position'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_skills', to='users.skill'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='states',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_states', to='users.state'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, null=True, related_name='customuser_user_permissions', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='departament',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='departament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_departament', to='users.departament'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
