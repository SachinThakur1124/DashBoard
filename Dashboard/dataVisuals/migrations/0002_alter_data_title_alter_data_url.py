# Generated by Django 5.0.6 on 2024-07-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisuals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(),
        ),
    ]
