# Generated by Django 5.1.6 on 2025-03-01 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nuhachillcare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhaiimodel',
            name='para_ac_brand',
            field=models.CharField(blank=True, choices=[('Daikin', 'daikin'), ('Samsung', 'samsung'), ('Bluestar', 'bluestar'), ('LG', 'lg'), ('Others', 'others')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bhaiimodel',
            name='para_ac_issue',
            field=models.CharField(blank=True, choices=[('Cooling Issues', 'cooling_issues'), ('Electrical Problems', 'electrical problems'), ('Water Leakage', 'water leakage'), ('Noisy Operation', 'noisy operation'), ('Others', 'others')], max_length=30, null=True),
        ),
    ]
