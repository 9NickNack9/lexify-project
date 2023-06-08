# Generated by Django 3.2.9 on 2023-02-05 11:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_b2brequest_b2crequest_employmentdocumentrequest_employmentnegotiationrequest_realestateconstructionr'),
    ]

    operations = [
        migrations.CreateModel(
            name='legalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_area', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('legalMonths', models.CharField(blank=True, choices=[('12', '12'), ('24', '24'), ('36', '36')], max_length=200, null=True)),
                ('legalHours', models.CharField(blank=True, choices=[('5 hours', '5 hours'), ('10 hours', '10 hours'), ('15 hours', '15 hours'), ('20 hours', '20 hours')], max_length=200, null=True)),
                ('legalOffers', models.CharField(blank=True, choices=[('Single hourly rate for occasional legal advice in the amount needed from time to time. Billed monthly in arrears.', 'Single hourly rate for occasional legal advice in the amount needed from time to time. Billed monthly in arrears.'), ('Lump sum monthly price for a fixed number of hours of legal support per month. Billed monthly in arrears.', 'Lump sum monthly price for a fixed number of hours of legal support per month. Billed monthly in arrears.')], max_length=200, null=True)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('b2bDate', models.DateField(null=True)),
                ('otherInfo', models.TextField(blank=True, null=True)),
                ('offerMaker', models.CharField(choices=[('Attorneys-at-law (FI: asianajotoimistot), any size', 'Attorneys-at-law (FI: asianajotoimistot), any size'), ('Attorneys-at-law, employing at least 5 lawyers', 'Attorneys-at-law, employing at least 5 lawyers'), ('Attorneys-at-law, employing at least 15 lawyers', 'Attorneys-at-law, employing at least 15 lawyers'), ('Law firms (FI: lakiasiaintoimistot), any size', 'Law firms (FI: lakiasiaintoimistot), any size'), ('Law firms, employing at least 5 lawyers', 'Law firms, employing at least 5 lawyers'), ('Law firms, employing at least 15 lawyers', 'Law firms, employing at least 15 lawyers')], max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('invoiceType', models.CharField(choices=[('On a monthly basis, invoice sent at end of each calendar month', 'On a monthly basis, invoice sent at end of each calendar month'), ('On a quarterly basis, invoice sent at end of each quarter', 'On a quarterly basis, invoice sent at end of each quarter'), ('One time invoice upon completion of the assignment', 'One time invoice upon completion of the assignment')], max_length=200, null=True)),
            ],
        ),
    ]