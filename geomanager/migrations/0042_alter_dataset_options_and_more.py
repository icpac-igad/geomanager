# Generated by Django 4.1.10 on 2024-01-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geomanager", "0041_dataset_order_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dataset",
            options={"ordering": ["order"], "verbose_name": "Dataset", "verbose_name_plural": "Datasets"},
        ),
        migrations.AlterField(
            model_name="rasterfilelayer",
            name="date_format",
            field=models.CharField(
                blank=True,
                choices=[
                    ("yyyy-MM-dd HH:mm", "Hour minute:second - (E.g 2023-01-01 00:00)"),
                    ("yyyy-MM-dd", "Day - (E.g 2023-01-01)"),
                    ("pentadal", "Pentadal - (E.g Jan 2023 - P1 1-5th)"),
                    ("yyyy-MM", "Month number - (E.g 2023-01)"),
                    ("MMMM yyyy", "Month name - (E.g January 2023)"),
                    ("yyyy", "Year - (E.g 2023)"),
                ],
                default="yyyy-MM-dd HH:mm",
                max_length=100,
                null=True,
                verbose_name="Display Format for DateTime Selector",
            ),
        ),
        migrations.AlterField(
            model_name="rastertilelayer",
            name="date_format",
            field=models.CharField(
                blank=True,
                choices=[
                    ("yyyy-MM-dd HH:mm", "Hour minute:second - (E.g 2023-01-01 00:00)"),
                    ("yyyy-MM-dd", "Day - (E.g 2023-01-01)"),
                    ("pentadal", "Pentadal - (E.g Jan 2023 - P1 1-5th)"),
                    ("yyyy-MM", "Month number - (E.g 2023-01)"),
                    ("MMMM yyyy", "Month name - (E.g January 2023)"),
                    ("yyyy", "Year - (E.g 2023)"),
                ],
                max_length=100,
                null=True,
                verbose_name="Display Format for DateTime Selector",
            ),
        ),
        migrations.AlterField(
            model_name="vectortilelayer",
            name="date_format",
            field=models.CharField(
                blank=True,
                choices=[
                    ("yyyy-MM-dd HH:mm", "Hour minute:second - (E.g 2023-01-01 00:00)"),
                    ("yyyy-MM-dd", "Day - (E.g 2023-01-01)"),
                    ("pentadal", "Pentadal - (E.g Jan 2023 - P1 1-5th)"),
                    ("yyyy-MM", "Month number - (E.g 2023-01)"),
                    ("MMMM yyyy", "Month name - (E.g January 2023)"),
                    ("yyyy", "Year - (E.g 2023)"),
                ],
                max_length=100,
                null=True,
                verbose_name="Display Format for DateTime Selector",
            ),
        ),
        migrations.AlterField(
            model_name="wmslayer",
            name="date_format",
            field=models.CharField(
                blank=True,
                choices=[
                    ("yyyy-MM-dd HH:mm", "Hour minute:second - (E.g 2023-01-01 00:00)"),
                    ("yyyy-MM-dd", "Day - (E.g 2023-01-01)"),
                    ("pentadal", "Pentadal - (E.g Jan 2023 - P1 1-5th)"),
                    ("yyyy-MM", "Month number - (E.g 2023-01)"),
                    ("MMMM yyyy", "Month name - (E.g January 2023)"),
                    ("yyyy", "Year - (E.g 2023)"),
                ],
                max_length=100,
                null=True,
                verbose_name="Display Format for DateTime Selector",
            ),
        ),
    ]
