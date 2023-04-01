# Generated by Django 4.1.7 on 2023-04-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mall", "0005_alter_cart_stuffs"),
    ]

    operations = [
        migrations.AddField(
            model_name="stuff", name="quantity", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="cart",
            name="stuffs",
            field=models.ManyToManyField(to="mall.stuff"),
        ),
    ]
