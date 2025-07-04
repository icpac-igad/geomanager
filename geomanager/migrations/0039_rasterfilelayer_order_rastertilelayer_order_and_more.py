# Generated by Django 4.1.10 on 2023-11-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geomanager", "0038_rasterfilelayer_legend_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="rasterfilelayer",
            name="order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="rastertilelayer",
            name="order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="vectorfilelayer",
            name="order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="vectortilelayer",
            name="order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="wmslayer",
            name="order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
