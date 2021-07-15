# Generated by Django 3.2.5 on 2021-07-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_item_meal_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='meal_category',
            field=models.CharField(blank=True, choices=[('main_course', 'Main Course'), ('drinks', 'Drinks'), ('starters', 'Starters')], max_length=50, null=True),
        ),
    ]
