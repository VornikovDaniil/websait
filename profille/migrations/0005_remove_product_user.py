# Generated by Django 5.0.7 on 2024-07-25 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profille', '0004_alter_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
