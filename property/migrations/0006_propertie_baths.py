# Generated by Django 4.2 on 2024-06-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_propertie_category_propertie_view_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertie',
            name='baths',
            field=models.IntegerField(default=0),
        ),
    ]
