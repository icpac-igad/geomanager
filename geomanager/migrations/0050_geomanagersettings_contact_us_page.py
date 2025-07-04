# Generated by Django 4.2.10 on 2024-04-23 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("geomanager", "0049_geomanagersettings_allow_signups_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="geomanagersettings",
            name="contact_us_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Contact Us Page",
            ),
        ),
    ]
