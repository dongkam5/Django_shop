# Generated by Django 4.1.7 on 2023-04-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mall", "0019_remove_cart_checked"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order", old_name="total", new_name="subtotal",
        ),
    ]
