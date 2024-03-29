# Generated by Django 3.2.9 on 2023-02-05 11:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20230205_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='B2BRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b2b_help', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('note', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('b2bDate', models.DateField(null=True)),
                ('otherInfo', models.TextField(blank=True, null=True)),
                ('offerMaker', models.CharField(choices=[('Attorneys-at-law (FI: asianajotoimistot), any size', 'Attorneys-at-law (FI: asianajotoimistot), any size'), ('Attorneys-at-law, employing at least 5 lawyers', 'Attorneys-at-law, employing at least 5 lawyers'), ('Attorneys-at-law, employing at least 15 lawyers', 'Attorneys-at-law, employing at least 15 lawyers'), ('Law firms (FI: lakiasiaintoimistot), any size', 'Law firms (FI: lakiasiaintoimistot), any size'), ('Law firms, employing at least 5 lawyers', 'Law firms, employing at least 5 lawyers'), ('Law firms, employing at least 15 lawyers', 'Law firms, employing at least 15 lawyers')], max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('invoiceType', models.CharField(choices=[('On a monthly basis, invoice sent at end of each calendar month', 'On a monthly basis, invoice sent at end of each calendar month'), ('On a quarterly basis, invoice sent at end of each quarter', 'On a quarterly basis, invoice sent at end of each quarter'), ('One time invoice upon completion of the assignment', 'One time invoice upon completion of the assignment')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='B2CRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b2c_help', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('note', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('b2bDate', models.DateField(null=True)),
                ('otherInfo', models.TextField(blank=True, null=True)),
                ('offerMaker', models.CharField(choices=[('Attorneys-at-law (FI: asianajotoimistot), any size', 'Attorneys-at-law (FI: asianajotoimistot), any size'), ('Attorneys-at-law, employing at least 5 lawyers', 'Attorneys-at-law, employing at least 5 lawyers'), ('Attorneys-at-law, employing at least 15 lawyers', 'Attorneys-at-law, employing at least 15 lawyers'), ('Law firms (FI: lakiasiaintoimistot), any size', 'Law firms (FI: lakiasiaintoimistot), any size'), ('Law firms, employing at least 5 lawyers', 'Law firms, employing at least 5 lawyers'), ('Law firms, employing at least 15 lawyers', 'Law firms, employing at least 15 lawyers')], max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('invoiceType', models.CharField(choices=[('On a monthly basis, invoice sent at end of each calendar month', 'On a monthly basis, invoice sent at end of each calendar month'), ('On a quarterly basis, invoice sent at end of each quarter', 'On a quarterly basis, invoice sent at end of each quarter'), ('One time invoice upon completion of the assignment', 'One time invoice upon completion of the assignment')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentDocumentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_docTemplate', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
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
            name='EmploymentNegotiationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employmentContract', models.CharField(choices=[('Employment Contract', 'Employment Contract'), ('Managing Director Contract', 'Managing Director Contract'), ('Mutual Termination Contract', 'Mutual Termination Contract')], max_length=200, null=True)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=5)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('employmentPos', models.TextField(blank=True, null=True)),
                ('b2bDate', models.DateField(null=True)),
                ('otherInfo', models.TextField(blank=True, null=True)),
                ('offerMaker', models.CharField(choices=[('Attorneys-at-law (FI: asianajotoimistot), any size', 'Attorneys-at-law (FI: asianajotoimistot), any size'), ('Attorneys-at-law, employing at least 5 lawyers', 'Attorneys-at-law, employing at least 5 lawyers'), ('Attorneys-at-law, employing at least 15 lawyers', 'Attorneys-at-law, employing at least 15 lawyers'), ('Law firms (FI: lakiasiaintoimistot), any size', 'Law firms (FI: lakiasiaintoimistot), any size'), ('Law firms, employing at least 5 lawyers', 'Law firms, employing at least 5 lawyers'), ('Law firms, employing at least 15 lawyers', 'Law firms, employing at least 15 lawyers')], max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('invoiceType', models.CharField(choices=[('On a monthly basis, invoice sent at end of each calendar month', 'On a monthly basis, invoice sent at end of each calendar month'), ('On a quarterly basis, invoice sent at end of each quarter', 'On a quarterly basis, invoice sent at end of each quarter'), ('One time invoice upon completion of the assignment', 'One time invoice upon completion of the assignment')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateConstructionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realConstruction', models.CharField(choices=[('Holistic legal representation throughout the transaction process (including but not limited to drafting of the construction agreement and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'), ('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'), ('First draft of the construction agreement, ready for delivery to the other party', '(c) First draft of construction agreement'), ('First draft of the construction agreement, ready for delivery to the other party and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of construction agreement + occasional support')], max_length=400, null=True)),
                ('constructionAgreement', models.CharField(choices=[('Contractor (seller of construction services)', 'Contractor (seller of construction services)'), ('Client (buyer of construction services)', 'Client (buyer of construction services)')], max_length=400, null=True)),
                ('constructionDescription', models.TextField(blank=True, null=True)),
                ('constructionPrice', models.CharField(choices=[('0 - 50kEUR', '0 - 50kEUR'), ('50 - 100kEUR', '50 - 100kEUR'), ('100kEUR - 1mEUR', '100kEUR - 1mEUR'), ('1+mEUR', '1+mEUR')], max_length=400, null=True)),
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
            name='RealEstateEasementRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constructionDescription', models.TextField(blank=True, null=True)),
                ('easementProperty', models.CharField(choices=[('Encumbered', 'Encumbered'), ('Encumbering', 'Encumbering')], max_length=400, null=True)),
                ('easementSupport', models.CharField(choices=[('Holistic legal representation throughout the easement agreement negotiation process (including but not limited to drafting of the easement agreement and related documents (excluding purely technical maps and other similar documents), required communications with the other property owner, participation in necessary easement related meetings with competent authorities, etc.)', '(a) Holistic legal representation'), ('Occasional support with the easement agreement negotiation process (e.g. commenting of the easement agreement documentation, legal advice during different stages of the process)', '(b) Occasional support'), ('First draft of the easement agreement (excluding purely technical maps and similar documents), ready for delivery to the other property owner', '(c) First draft of lease agreement'), ('First draft of the easement agreement (excluding purely technical maps and similar documents), ready for delivery to the other property owner and thereafter occasional support with the easement agreement process (e.g. further commenting of the easement agreement documentation, legal advice during different stages of the process)', '(d) First draft of lease agreement + occasional support')], max_length=400, null=True)),
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
            name='RealEstateLeasebackRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leasebackSeller', models.CharField(choices=[('Seller and Tenant', 'Seller and Tenant'), ('Buyer and Landlord', 'Buyer and Landlord')], max_length=400, null=True)),
                ('leasebackDescription', models.TextField(blank=True, null=True)),
                ('leasebackRange', models.CharField(choices=[('0-100 kEUR', '0-100 kEUR'), ('100 kEUR - 1 mEUR', '100 kEUR - 1 mEUR'), ('1-10 mEUR', '1-10 mEUR'), ('10-50 mEUR', '10-50 mEUR'), ('50+ mEUR', '50+ mEUR')], max_length=400, null=True)),
                ('leasebackInspection', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=400, null=True)),
                ('realLeaseBack', models.CharField(choices=[('Holistic legal representation throughout the transaction process (including but not limited to drafting of the sale and leaseback agreement and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'), ('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'), ('First draft of the sale and leaseback agreement, ready for delivery to the other party', '(c) First draft of sale and purchase and lease agreement'), ('First draft of the sale and leaseback agreement, ready for delivery to the other party and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of sale and purchase and lease agreement + occasional support')], max_length=400, null=True)),
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
            name='RealEstateLeaseRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realLease', models.CharField(choices=[('Holistic legal representation throughout the transaction process (including but not limited to drafting of the lease and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'), ('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'), ('First draft of the lease agreement, ready for delivery to the other party', '(c) First draft of lease agreement'), ('First draft of the lease agreement, ready for delivery to the other party and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of lease agreement + occasional support')], max_length=400, null=True)),
                ('leaseAgreement', models.CharField(choices=[('Lease of business premises', 'Lease of business premises'), ('Lease of residential premises', 'Lease of residential premises'), ('Lease of a plot or a parcel of land', 'Lease of a plot or a parcel of land')], max_length=400, null=True)),
                ('leaseRole', models.CharField(choices=[('Tenant', 'Tenant'), ('Landlord', 'Landlord')], max_length=400, null=True)),
                ('leaseDescription', models.TextField(blank=True, null=True)),
                ('leaseRange', models.CharField(choices=[('0-1000 EUR', '0-1000 EUR'), ('1000 EUR-10 000 EUR', '1000 EUR-10 000 EUR'), ('10 000 EUR-50 000 EUR', '10 000 EUR-50 000 EUR'), ('50 000 EUR+', '50 000 EUR+')], max_length=400, null=True)),
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
            name='RealEstatePurchaseRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realestateAgreement', models.CharField(choices=[('Plot/Parcel of Land', 'Plot/Parcel of Land'), ('Shares in a Real Estate Company (FI: kiinteistöosakeyhtiö)', 'Shares in a Real Estate Company (FI: kiinteistöosakeyhtiö)'), ('Shares in a Housing Association (FI: asunto-osakeyhtiö)', 'Shares in a Housing Association (FI: asunto-osakeyhtiö)')], max_length=400, null=True)),
                ('agreementBuyer', models.CharField(choices=[('Buying', 'Buying'), ('Selling', 'Selling')], max_length=400, null=True)),
                ('agreementDescription', models.TextField(blank=True, null=True)),
                ('agreementRange', models.CharField(choices=[('0-100 kEUR', '0-100 kEUR'), ('100 kEUR - 1 mEUR', '100 kEUR - 1 mEUR'), ('1-10 mEUR', '1-10 mEUR'), ('10-50 mEUR', '10-50 mEUR'), ('50+ mEUR', '50+ mEUR')], max_length=400, null=True)),
                ('agreementInspection', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=400, null=True)),
                ('realSalePurchase', models.CharField(choices=[('Holistic legal representation throughout the transaction process (including but not limited to drafting of the sale and purchase agreement and related documents, required negotiations with the other party and completion of signing/closing related legal actions)', '(a) Holistic legal representation'), ('Occasional support with the transaction process (e.g. commenting of transactional documents, legal advice during different stages of the transaction)', '(b) Occasional support'), ('First draft of the sale and purchase agreement, ready for delivery to the other party', '(c) First draft of sale and purchase agreement'), ('First draft of the sale and purchase agreement, ready for delivery to the buyer/seller and thereafter occasional support with the transaction process (e.g. further commenting of transactional documents, legal advice during different stages of the transaction)', '(d) First draft of sale and purchase agreement + occasional support')], max_length=400, null=True)),
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
            name='sourcingBusTemplateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourcingTemplate', models.CharField(choices=[('Products', 'Products'), ('Services', 'Services')], max_length=400, null=True)),
                ('sourcingGeneric', models.CharField(choices=[('Generic', 'Generic'), ('Customized', 'Customized')], max_length=400, null=True)),
                ('sourcingCustomized', models.TextField(blank=True, null=True)),
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
            name='sourcingSupAgreementRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourcingLawyer', models.TextField(blank=True, null=True)),
                ('sourcingType', models.CharField(choices=[('My own contract template', 'My own contract template'), ("Supplier's contract template", "Supplier's contract template")], max_length=400, null=True)),
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
            name='sourcingSupTemplateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourcingComments', models.TextField(blank=True, null=True)),
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
