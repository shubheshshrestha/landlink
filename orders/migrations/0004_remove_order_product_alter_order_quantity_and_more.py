# Generated by Django 5.1.6 on 2025-03-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('returned', 'Returned'), ('shipped', 'Shipped'), ('processing', 'Processing'), ('pending', 'Pending'), ('cancelled', 'Cancelled'), ('delivered', 'Delivered')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
