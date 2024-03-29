# Generated by Django 4.2.3 on 2024-02-09 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopzero', '0007_remove_cart_items_remove_cartitem_user_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shopzero.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
