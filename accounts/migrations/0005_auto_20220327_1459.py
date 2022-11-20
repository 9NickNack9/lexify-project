# Generated by Django 3.2.9 on 2022-03-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220319_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='additionalInfo',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='hourCount',
            field=models.CharField(choices=[('Corporate law (0-5 hours)', 'Corporate law (0-5 hours)'), ('Employment law (10 hours)', 'Employment law (10 hours)'), ('IFR (20 hours)', 'IFR (20 hours)')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='invoiceType',
            field=models.CharField(choices=[('On a monthly basis', 'On a monthly basis'), ('On a quarterly basis', 'On a quarterly basis'), ('One time invoice (upon completion of the assignment)', 'One time invoice (upon completion of the assignment)')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Finnish', 'Finnish'), ('Swedish', 'Swedish'), ('English & Finnish', 'English & Finnish')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='offerMaker',
            field=models.CharField(choices=[('Legal Office (lakiasiaintoimisto)', 'Legal Office (lakiasiaintoimisto)'), ('Law Firm (asianajotoimisto)', 'Law Firm (asianajotoimisto)'), ('Finland Top 15 law firm (Based on number of lawyers)', 'Finland Top 15 law firm (Based on number of lawyers)')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='offerTime',
            field=models.CharField(choices=[('In 24 hours', 'In 24 hours'), ('In 48 hours', 'In 48 hours'), ('In 7 days', 'In 7 days')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='requestType',
            field=models.CharField(choices=[('Contract(s)', 'Contract(s)'), ('Day-to-day legal advice', 'Day-to-day legal advice'), ('Support with dispute resolution', 'Support with dispute resolution'), ('Support with M&A', 'Support with M&A'), ('Support with corporate governance', 'Support with corporate governance')], max_length=200, null=True),
        ),
    ]