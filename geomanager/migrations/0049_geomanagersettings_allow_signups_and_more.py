# Generated by Django 4.2.10 on 2024-04-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0048_alter_geomanagersettings_map_disclaimer_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='geomanagersettings',
            name='allow_signups',
            field=models.BooleanField(default=False, verbose_name='Allow user signups'),
        ),
        migrations.AddField(
            model_name='geomanagersettings',
            name='enable_my_account',
            field=models.BooleanField(default=False, verbose_name='Enable My Account'),
        ),
    ]
