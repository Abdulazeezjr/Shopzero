# Generated by Django 4.2.3 on 2024-02-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopzero', '0015_remove_wishlistitem_id_wishlistitem_wishlistitem_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='wishlistitem_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]