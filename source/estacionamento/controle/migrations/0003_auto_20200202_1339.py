# Generated by Django 3.0.2 on 2020-02-02 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20200202_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parking',
            old_name='license_plate',
            new_name='plate',
        ),
        migrations.RenameField(
            model_name='parking',
            old_name='reservation_number',
            new_name='reservation',
        ),
    ]
