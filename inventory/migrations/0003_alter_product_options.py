# Generated by Django 4.2.4 on 2023-08-05 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]
