# Generated by Django 3.2.9 on 2022-02-19 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('requestType', models.CharField(choices=[('Contract', 'Contract'), ('Day-to-day advice per month', 'Day-to-day advice per month'), ('Family documents', 'Family documents'), ('Inheritance documents', 'Inheritance documents'), ('Insolvency documents', 'Insolvency documents'), ('Other', 'Other')], max_length=200, null=True)),
                ('contractType', models.CharField(choices=[('Share trade document', 'Share trade document'), ('APA', 'APA')], max_length=200, null=True)),
                ('hourCount', models.CharField(choices=[('Corporate law (0-5 hours)', 'Corporate law (0-5 hours)'), ('Employment law (10 hours)', 'Employment law (10 hours)'), ('IFR (20 hours)', 'IFR (20 hours)'), ('Other', 'Other')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='offer',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
    ]
