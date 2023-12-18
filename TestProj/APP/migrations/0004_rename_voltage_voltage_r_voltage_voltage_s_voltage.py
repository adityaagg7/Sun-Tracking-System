# Generated by Django 4.2.5 on 2023-12-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_delete_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voltage',
            old_name='voltage',
            new_name='r_voltage',
        ),
        migrations.AddField(
            model_name='voltage',
            name='s_voltage',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
