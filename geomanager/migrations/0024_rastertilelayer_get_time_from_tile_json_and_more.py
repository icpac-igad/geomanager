# Generated by Django 4.1.10 on 2023-10-04 09:27

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks
import wagtailiconchooser.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("geomanager", "0023_vectortilelayericon"),
    ]

    operations = [
        migrations.AddField(
            model_name="rastertilelayer",
            name="get_time_from_tile_json",
            field=models.BooleanField(default=False, verbose_name="Get time from tile json url"),
        ),
        migrations.AddField(
            model_name="rastertilelayer",
            name="tile_json_url",
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name="Tile JSON url"),
        ),
        migrations.AddField(
            model_name="rastertilelayer",
            name="timestamps_response_object_key",
            field=models.CharField(
                blank=True,
                default="timestamps",
                help_text="Key for timestamps values in response object",
                max_length=100,
                null=True,
                verbose_name="Timestamps response object key",
            ),
        ),
        migrations.AddField(
            model_name="vectortilelayer",
            name="get_time_from_tile_json",
            field=models.BooleanField(default=False, verbose_name="Get time from tile json url"),
        ),
        migrations.AddField(
            model_name="vectortilelayer",
            name="tile_json_url",
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name="Tile JSON url"),
        ),
        migrations.AddField(
            model_name="vectortilelayer",
            name="timestamps_response_object_key",
            field=models.CharField(
                blank=True,
                default="timestamps",
                help_text="Key for timestamps values in response object",
                max_length=100,
                null=True,
                verbose_name="Timestamps response object key",
            ),
        ),
        migrations.AlterField(
            model_name="rastertilelayer",
            name="legend",
            field=wagtail.fields.StreamField(
                [
                    (
                        "legend",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "type",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("basic", "Basic"),
                                            ("gradient", "Gradient"),
                                            ("choropleth", "Choropleth"),
                                        ],
                                        label="Legend Type",
                                    ),
                                ),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "value",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Can be a number or text e.g '10' or '10-20' or 'Vegetation'",
                                                        label="value",
                                                    ),
                                                ),
                                                (
                                                    "color",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Color value e.g rgb(73,73,73) or #494949",
                                                        label="color",
                                                    ),
                                                ),
                                            ]
                                        ),
                                        label="Legend Items",
                                        min_num=1,
                                    ),
                                ),
                            ],
                            label="Custom Legend",
                        ),
                    ),
                    ("legend_image", wagtail.images.blocks.ImageChooserBlock(label="Custom Image")),
                    (
                        "legend_icon",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "icon_image",
                                                    wagtailiconchooser.blocks.IconChooserBlock(label="Icon Image"),
                                                ),
                                                ("icon_label", wagtail.blocks.CharBlock(label="Icon Label")),
                                                (
                                                    "icon_color",
                                                    wagtail_color_panel.blocks.NativeColorBlock(
                                                        default="#000000", label="Icon color", required=False
                                                    ),
                                                ),
                                            ]
                                        ),
                                        label="Legend Icons",
                                        min_num=1,
                                    ),
                                )
                            ],
                            label="Legend Icon",
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Legend",
            ),
        ),
        migrations.AlterField(
            model_name="vectortilelayer",
            name="legend",
            field=wagtail.fields.StreamField(
                [
                    (
                        "legend",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "type",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("basic", "Basic"),
                                            ("gradient", "Gradient"),
                                            ("choropleth", "Choropleth"),
                                        ],
                                        label="Legend Type",
                                    ),
                                ),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "value",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Can be a number or text e.g '10' or '10-20' or 'Vegetation'",
                                                        label="value",
                                                    ),
                                                ),
                                                (
                                                    "color",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Color value e.g rgb(73,73,73) or #494949",
                                                        label="color",
                                                    ),
                                                ),
                                            ]
                                        ),
                                        label="Legend Items",
                                        min_num=1,
                                    ),
                                ),
                            ],
                            label="Custom Legend",
                        ),
                    ),
                    ("legend_image", wagtail.images.blocks.ImageChooserBlock(label="Custom Image")),
                    (
                        "legend_icon",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "icon_image",
                                                    wagtailiconchooser.blocks.IconChooserBlock(label="Icon Image"),
                                                ),
                                                ("icon_label", wagtail.blocks.CharBlock(label="Icon Label")),
                                                (
                                                    "icon_color",
                                                    wagtail_color_panel.blocks.NativeColorBlock(
                                                        default="#000000", label="Icon color", required=False
                                                    ),
                                                ),
                                            ]
                                        ),
                                        label="Legend Icons",
                                        min_num=1,
                                    ),
                                )
                            ],
                            label="Legend Icon",
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Legend",
            ),
        ),
    ]
