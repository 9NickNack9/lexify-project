# Generated by Django 3.2.9 on 2023-04-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20230308_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmenttemplaterequest',
            name='priceOffer',
            field=models.CharField(max_length=300, null=True),
        ),
    ]