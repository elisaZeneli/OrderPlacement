# Generated by Django 3.2.5 on 2021-08-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_orderimage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderimage',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
