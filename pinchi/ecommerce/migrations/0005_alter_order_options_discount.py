# Generated by Django 5.0.1 on 2024-02-01 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_placed'], 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, help_text='Discount percentage for the product category and user category.', max_digits=5, verbose_name='Percentage Discount')),
                ('user_category', models.CharField(choices=[('BRONZE', 20), ('SILVER', 49)], max_length=50, verbose_name='User Category')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.category', verbose_name='Product Category')),
            ],
        ),
    ]