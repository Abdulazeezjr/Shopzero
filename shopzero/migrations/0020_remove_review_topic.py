# Generated by Django 4.2.3 on 2024-02-15 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopzero', '0019_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='topic',
        ),
    ]
