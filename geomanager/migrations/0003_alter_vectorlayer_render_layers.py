# Generated by Django 4.2.1 on 2023-05-17 14:45

import django.core.validators
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0002_vectorlayer_render_layers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vectorlayer',
            name='render_layers',
            field=wagtail.fields.StreamField([('fill', wagtail.blocks.StructBlock([('filter', wagtail.blocks.CharBlock(label='filter', required=False)), ('maxzoom', wagtail.blocks.IntegerBlock(label='maxzoom', required=False)), ('minzoom', wagtail.blocks.IntegerBlock(label='minzoom', required=False)), ('paint', wagtail.blocks.StructBlock([('fill_antialias', wagtail.blocks.BooleanBlock(default=True, label='fill antialias', required=False)), ('fill_color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000', label='fill color')), ('fill_opacity', wagtail.blocks.IntegerBlock(default=1, label='fill opacity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])), ('fill_outline_color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000', label='fill outline color'))], label='Paint Properties'))], label='Fill Layer')), ('line', wagtail.blocks.StructBlock([('filter', wagtail.blocks.CharBlock(label='filter', required=False)), ('maxzoom', wagtail.blocks.IntegerBlock(label='maxzoom', required=False)), ('minzoom', wagtail.blocks.IntegerBlock(label='minzoom', required=False)), ('paint', wagtail.blocks.StructBlock([('line_color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000', label='line color')), ('line_opacity', wagtail.blocks.IntegerBlock(default=1, label='line opacity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])), ('line_width', wagtail.blocks.IntegerBlock(default=1, label='line_width', validators=[django.core.validators.MinValueValidator(0)]))], label='Paint Properties'))], label='Line Layer')), ('circle', wagtail.blocks.StructBlock([('filter', wagtail.blocks.CharBlock(label='filter', required=False)), ('maxzoom', wagtail.blocks.IntegerBlock(label='maxzoom', required=False)), ('minzoom', wagtail.blocks.IntegerBlock(label='minzoom', required=False)), ('paint', wagtail.blocks.StructBlock([('circle_color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000', label='circle color')), ('circle_opacity', wagtail.blocks.IntegerBlock(default=1, label='circle opacity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])), ('circle_radius', wagtail.blocks.IntegerBlock(default=5, label='circle radius', validators=[django.core.validators.MinValueValidator(0)])), ('circle_stroke_color', wagtail_color_panel.blocks.NativeColorBlock(default='#000000', label='circle stroke color')), ('circle_stroke_width', wagtail.blocks.IntegerBlock(default=0, label='circle_stroke_width', validators=[django.core.validators.MinValueValidator(0)]))], label='Paint Properties'))], label='Point/Circle Layer'))], blank=True, null=True, use_json_field=True, verbose_name='Render Layers'),
        ),
    ]
