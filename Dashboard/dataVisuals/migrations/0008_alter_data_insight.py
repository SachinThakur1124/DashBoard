# Generated by Django 5.0.6 on 2024-07-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisuals', '0007_alter_data_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='insight',
            field=models.CharField(max_length=255),
        ),
    ]
