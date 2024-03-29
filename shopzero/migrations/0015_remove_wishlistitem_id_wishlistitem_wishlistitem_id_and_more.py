# Generated by Django 4.2.3 on 2024-02-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopzero', '0014_rename_wishlistitems_wishlistitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='id',
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='wishlistitem_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='items',
            field=models.ManyToManyField(blank=True, default=None, to='shopzero.wishlistitem'),
        ),
    ]
