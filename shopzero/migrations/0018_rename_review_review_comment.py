# Generated by Django 4.2.3 on 2024-02-13 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopzero', '0017_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='comment',
        ),
    ]
