# Generated by Django 4.0 on 2022-01-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0008_doctor_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='img',
            field=models.CharField(blank=True, default='https://www.jupiterhospital.com/uploadedfiles/gallery/1584607002_male-dummy.jpg', max_length=1000, null=True),
        ),
    ]