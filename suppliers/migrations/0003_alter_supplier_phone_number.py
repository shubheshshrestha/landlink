# Generated by Django 5.1.6 on 2025-03-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_supplier_address_supplier_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
