# Generated by Django 4.0 on 2021-12-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_remove_doctor_gender_doctor_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
    ]
