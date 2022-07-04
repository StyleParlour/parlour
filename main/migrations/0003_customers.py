# Generated by Django 4.0.5 on 2022-06-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_offers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('cId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('token', models.IntegerField()),
                ('isVerified', models.BooleanField(default=False)),
                ('dateCreated', models.DateField(auto_now_add=True)),
            ],
        ),
    ]