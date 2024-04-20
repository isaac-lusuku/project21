# Generated by Django 4.2.11 on 2024-04-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0004_rename_city_business_location_business_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.TextField(default='all', max_length=255),
        ),
        migrations.AlterField(
            model_name='business',
            name='delivery_options',
            field=models.TextField(blank=True, max_length=235, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.TextField(blank=True, max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
