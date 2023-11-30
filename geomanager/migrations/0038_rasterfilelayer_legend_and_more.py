# Generated by Django 4.1.10 on 2023-11-30 14:01

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0037_dataset_enable_all_multi_layers_on_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasterfilelayer',
            name='legend',
            field=wagtail.fields.StreamField([('legend', wagtail.blocks.StructBlock([('type', wagtail.blocks.ChoiceBlock(choices=[('basic', 'Basic'), ('gradient', 'Gradient'), ('choropleth', 'Choropleth')], label='Legend Type')), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('value', wagtail.blocks.CharBlock(help_text="Can be a number or text e.g '10' or '10-20' or 'Vegetation'", label='value')), ('color', wagtail.blocks.CharBlock(help_text='Color value e.g rgb(73,73,73) or #494949', label='color'))]), label='Legend Items', min_num=1))], label='Custom Legend')), ('legend_image', wagtail.images.blocks.ImageChooserBlock(label='Custom Image'))], blank=True, null=True, use_json_field=True, verbose_name='Legend'),
        ),
        migrations.AddField(
            model_name='rasterfilelayer',
            name='use_custom_legend',
            field=models.BooleanField(default=False, verbose_name='Use custom legend'),
        ),
    ]
