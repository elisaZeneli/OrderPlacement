# Generated by Django 3.2.5 on 2021-07-13 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': (('can_add_row', 'Can add new rows'), ('can_update_row', 'Can update rows'), ('can_delete_rows', 'Can delete rows'))},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': (('can_add_row', 'Can add new rows'), ('can_update_row', 'Can update rows'), ('can_delete_rows', 'Can delete rows'), ('can_view_info', 'Can view info'), ('can_view_others_info', 'Can view others info'))},
        ),
    ]