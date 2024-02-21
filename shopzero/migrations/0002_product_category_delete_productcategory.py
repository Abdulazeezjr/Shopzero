# Generated by Django 4.2.3 on 2024-02-08 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopzero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopzero.category'),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
