# Generated by Django 4.2.4 on 2023-08-30 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_bookappointment_confirm_bookappointment_payment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookAppointment',
        ),
    ]
