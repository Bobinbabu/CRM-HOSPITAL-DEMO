# Generated by Django 4.2.9 on 2024-07-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0007_newleads'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clinic3', models.CharField(max_length=50)),
                ('VATnumber3', models.CharField(max_length=50)),
                ('Phone3', models.CharField(max_length=50)),
                ('Website3', models.CharField(max_length=50)),
                ('Group3', models.CharField(max_length=50)),
                ('Currency3', models.CharField(max_length=50)),
                ('Language3', models.CharField(max_length=50)),
                ('Address3', models.CharField(max_length=50)),
                ('City3', models.CharField(max_length=50)),
                ('State3', models.CharField(max_length=50)),
                ('Zipcode3', models.CharField(max_length=50)),
                ('Country3', models.CharField(max_length=50)),
            ],
        ),
    ]
