# Generated by Django 3.2.9 on 2022-06-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220605_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='corpPreparation',
        ),
        migrations.RemoveField(
            model_name='request',
            name='legalAreas',
        ),
        migrations.AddField(
            model_name='request',
            name='mergerCompany',
            field=models.CharField(blank=True, choices=[('Shares', 'Shares'), ('Business', 'Business'), ('Specific asset(s)', 'Specific asset(s)')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='mergerType',
            field=models.CharField(blank=True, choices=[('Shares', 'Shares'), ('Business', 'Business'), ('Specific asset(s)', 'Specific asset(s)')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='sellOrBuy',
            field=models.CharField(blank=True, choices=[('Buying', 'Buying'), ('Selling', 'Selling')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='legalHours',
            field=models.CharField(blank=True, choices=[('5 hours', '5 hours'), ('10 hours', '10 hours'), ('15 hours', '15 hours'), ('20 hours', '20 hours')], max_length=200, null=True),
        ),
    ]