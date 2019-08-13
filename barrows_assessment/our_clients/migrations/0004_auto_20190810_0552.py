# Generated by Django 2.2 on 2019-08-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_clients', '0003_auto_20190809_0517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='owner',
            new_name='client_name',
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_status',
            field=models.CharField(choices=[('', 'Select Status'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('Complete', 'Complete')], max_length=100),
        ),
    ]