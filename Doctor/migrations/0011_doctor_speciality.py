# Generated by Django 4.0 on 2022-01-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0010_alter_doctor_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
