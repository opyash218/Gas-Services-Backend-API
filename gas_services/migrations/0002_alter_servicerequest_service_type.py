# Generated by Django 5.1.7 on 2025-03-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(max_length=50),
        ),
    ]
