# Generated by Django 3.2.9 on 2023-02-12 10:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_legalrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='disputeArbitrationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispRole', models.CharField(blank=True, choices=[('Claimant', 'Claimant'), ('Defendant', 'Defendant')], max_length=200, null=True)),
                ('arbiArea', models.CharField(blank=True, choices=[('Holistic legal representation in arbitration proceedings (including e.g. drafting of legal briefs, representation in arbitration hearings, attorney-client communications)', '(a) Holistic legal representation in arbitration proceedings'), ('Occasional support with arbitration proceedings (e.g. commenting on legal briefs, periodic advice regarding legal strategy, etc.)', '(b) Occasional support with arbitration proceedings')], max_length=200, null=True)),
                ('dispDescription', models.TextField(null=True)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('b2bDate', models.DateField(null=True)),
                ('otherInfo', models.TextField(blank=True, null=True)),
                ('offerMaker', models.CharField(choices=[('Attorneys-at-law (FI: asianajotoimistot), any size', 'Attorneys-at-law (FI: asianajotoimistot), any size'), ('Attorneys-at-law, employing at least 5 lawyers', 'Attorneys-at-law, employing at least 5 lawyers'), ('Attorneys-at-law, employing at least 15 lawyers', 'Attorneys-at-law, employing at least 15 lawyers'), ('Law firms (FI: lakiasiaintoimistot), any size', 'Law firms (FI: lakiasiaintoimistot), any size'), ('Law firms, employing at least 5 lawyers', 'Law firms, employing at least 5 lawyers'), ('Law firms, employing at least 15 lawyers', 'Law firms, employing at least 15 lawyers')], max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('invoiceType', models.CharField(choices=[('On a monthly basis, invoice sent at end of each calendar month', 'On a monthly basis, invoice sent at end of each calendar month'), ('On a quarterly basis, invoice sent at end of each quarter', 'On a quarterly basis, invoice sent at end of each quarter'), ('One time invoice upon completion of the assignment', 'One time invoice upon completion of the assignment')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='disputeCourtRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispRole', models.CharField(blank=True, choices=[('Claimant', 'Claimant'), ('Defendant', 'Defendant')], max_length=200, null=True)),
                ('courtArea', models.CharField(blank=True, choices=[('Holistic legal representation in court proceedings (including e.g. drafting of legal briefs, representation in court hearings, attorney-client communications)', '(a) Holistic legal representation in court proceedings'), ('Occasional support with court proceedings (e.g. commenting on legal briefs, periodic advice regarding legal strategy, etc.)', '(b) Occasional support with court proceedings')], max_length=200, null=True)),
                ('dispDescription', models.TextField(null=True)),
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