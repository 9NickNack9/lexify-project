# Generated by Django 3.2.9 on 2023-03-01 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20230216_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
