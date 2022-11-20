# Generated by Django 3.2.9 on 2022-08-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220731_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='arbiRole',
            new_name='dispRole',
        ),
        migrations.RemoveField(
            model_name='request',
            name='courtRole',
        ),
        migrations.AddField(
            model_name='request',
            name='dispArea',
            field=models.CharField(blank=True, choices=[('Court Proceedings Holistic legal representation', '(a) Court Proceedings Holistic legal representation'), ('Court Proceedings Occasional support', '(b) Court Proceedings Occasional support'), ('Arbitration Proceedings Holistic legal representation', '(c) Arbitration Proceedings Holistic legal representation'), ('Arbitration Proceedings Occasional support', '(d) Arbitration Proceedings Occasional support'), ('Settlement Negotiations Holistic legal representation', '(e) Settlement Negotiations Court Proceedings Holistic legal representation'), ('Settlement Negotiations Occasional support', '(f) Settlement Negotiations Court Proceedings Occasional support')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='dispParty',
            field=models.CharField(blank=True, choices=[('a Party to Court Proceedings', 'a Party to Court Proceedings'), ('a Party to Arbitration Proceedings', 'a Party to Arbitration Proceedings'), ('a Party to Settlement Negotiations', 'a Party to Settlement Negotiations')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='arbiArea',
            field=models.CharField(blank=True, choices=[('Court Proceedings Holistic legal representation', '(a) Court Proceedings Holistic legal representation'), ('Court Proceedings Occasional support', '(b) Court Proceedings Occasional support'), ('Arbitration Proceedings Holistic legal representation', '(c) Arbitration Proceedings Holistic legal representation'), ('Arbitration Proceedings Occasional support', '(d) Arbitration Proceedings Occasional support'), ('Settlement Negotiations Holistic legal representation', '(e) Settlement Negotiations Court Proceedings Holistic legal representation'), ('Settlement Negotiations Occasional support', '(f) Settlement Negotiations Court Proceedings Occasional support')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='courtArea',
            field=models.CharField(blank=True, choices=[('Court Proceedings Holistic legal representation', '(a) Court Proceedings Holistic legal representation'), ('Court Proceedings Occasional support', '(b) Court Proceedings Occasional support'), ('Arbitration Proceedings Holistic legal representation', '(c) Arbitration Proceedings Holistic legal representation'), ('Arbitration Proceedings Occasional support', '(d) Arbitration Proceedings Occasional support'), ('Settlement Negotiations Holistic legal representation', '(e) Settlement Negotiations Court Proceedings Holistic legal representation'), ('Settlement Negotiations Occasional support', '(f) Settlement Negotiations Court Proceedings Occasional support')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='mergerArea',
            field=models.CharField(blank=True, choices=[('Holistic legal representation', '(1) Holistic legal representation'), ('Occasional support', '(2) Occasional support'), ('Short form LDD report', '(3) Short form LDD report'), ('Long form LDD report', '(4) Long form LDD report')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='privacyOptions',
            field=models.CharField(choices=[('Holistic review', '(a) Holistic review'), ('Holistic review + performance of corrective actions', '(b) Holistic review + performance of corrective actions')], max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='settlementArea',
            field=models.CharField(blank=True, choices=[('Court Proceedings Holistic legal representation', '(a) Court Proceedings Holistic legal representation'), ('Court Proceedings Occasional support', '(b) Court Proceedings Occasional support'), ('Arbitration Proceedings Holistic legal representation', '(c) Arbitration Proceedings Holistic legal representation'), ('Arbitration Proceedings Occasional support', '(d) Arbitration Proceedings Occasional support'), ('Settlement Negotiations Holistic legal representation', '(e) Settlement Negotiations Court Proceedings Holistic legal representation'), ('Settlement Negotiations Occasional support', '(f) Settlement Negotiations Court Proceedings Occasional support')], max_length=200, null=True),
        ),
    ]
