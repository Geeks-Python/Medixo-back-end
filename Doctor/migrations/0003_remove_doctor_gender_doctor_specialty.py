# Generated by Django 4.0 on 2021-12-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_rename_country_doctor_building_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='gender',
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(choices=[('Anesthesiology', 'Anesthesiology'), ('Neurology', 'Neurology'), ('Pathology', 'Pathology'), ('Surgery', 'Surgery')], max_length=100, null=True),
        ),
    ]