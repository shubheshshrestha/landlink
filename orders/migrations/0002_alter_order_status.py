# Generated by Django 5.1.6 on 2025-03-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'Delivered'), ('shipped', 'Shipped'), ('processing', 'Processing'), ('pending', 'Pending'), ('cancelled', 'Cancelled'), ('returned', 'Returned')], default='pending', max_length=20),
        ),
    ]
