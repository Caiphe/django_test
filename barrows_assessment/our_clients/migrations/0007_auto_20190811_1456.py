# Generated by Django 2.2 on 2019-08-11 14:56

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('our_clients', '0006_auto_20190811_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='contact_number',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=100),
        ),
    ]
