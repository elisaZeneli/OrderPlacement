# Generated by Django 3.2.5 on 2021-08-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20210817_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderimage',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]