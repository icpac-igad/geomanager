# Generated by Django 4.2 on 2025-04-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0051_rasterstyle_rendering_engine'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='dataset_slug',
            field=models.CharField(blank=True, help_text='A human-readable hypen separated text to uniquely identify the dataset for the purpose of updating from data ingestion jobs and visualization using mapserver/mapcache', max_length=200, null=True, verbose_name='human-readable dataset unique identifier text'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='latest_date',
            field=models.DateField(blank=True, help_text='Last day date of the pentad/week/dekad/month/season as extracted from dataset, depending on dataset periodicity', null=True, verbose_name='latest data date set by data ingestion job'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='current_time_method',
            field=models.CharField(choices=[('latest_from_source', 'Latest available date from source'), ('earliest_from_source', 'Earliest available date from source'), ('previous_to_now', 'Date previous to current date time'), ('next_to_now', 'Date next to current date time'), ('from_dataset_props', 'Dataset model property set by data ingestion job')], default='latest_from_source', help_text='How to pick default time and for updates, for Multi-Temporal data', max_length=100, verbose_name='current time method'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='summary',
            field=models.CharField(blank=True, help_text='Short dataset summary of less than 100 characters', max_length=100, null=True, verbose_name='summary'),
        ),
    ]
