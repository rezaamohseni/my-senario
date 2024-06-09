# Generated by Django 4.2 on 2024-06-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='propertie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='property_default.jpg', upload_to='property')),
                ('title', models.CharField(max_length=100)),
                ('rent', models.IntegerField()),
                ('area', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('garages', models.IntegerField()),
            ],
        ),
    ]