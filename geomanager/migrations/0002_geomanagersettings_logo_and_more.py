# Generated by Django 4.2.1 on 2023-06-08 08:23

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("geomanager", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="geomanagersettings",
            name="logo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Logo",
            ),
        ),
        migrations.AddField(
            model_name="geomanagersettings",
            name="navigation",
            field=wagtail.fields.StreamField(
                [
                    (
                        "menu_items",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    ("label", wagtail.blocks.CharBlock(label="Label")),
                                    (
                                        "page",
                                        wagtail.blocks.PageChooserBlock(label="Page"),
                                    ),
                                ]
                            )
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
