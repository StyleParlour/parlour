# Generated by Django 4.0.5 on 2022-07-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_booking_cid_remove_booking_sid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='slotDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='slotTime',
            field=models.TimeField(null=True),
        ),
    ]
