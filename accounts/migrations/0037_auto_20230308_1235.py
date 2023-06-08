# Generated by Django 3.2.9 on 2023-03-08 10:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_alter_customer_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2brequest',
            name='b2b_help',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=5),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]