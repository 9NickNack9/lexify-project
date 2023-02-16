# Generated by Django 3.2.9 on 2023-02-05 10:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20230124_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='employment_conTemplate',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5),
        ),
        migrations.AlterField(
            model_name='request',
            name='language',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5),
        ),
    ]
