# Generated by Django 5.1.6 on 2025-04-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
