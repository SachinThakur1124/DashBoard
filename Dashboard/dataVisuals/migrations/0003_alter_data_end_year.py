# Generated by Django 5.0.6 on 2024-07-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisuals', '0002_alter_data_title_alter_data_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.CharField(max_length=40),
        ),
    ]
