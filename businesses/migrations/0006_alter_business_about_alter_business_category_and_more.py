# Generated by Django 4.2.11 on 2024-04-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0005_alter_business_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='about',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.TextField(default='all', max_length=500),
        ),
        migrations.AlterField(
            model_name='business',
            name='delivery_options',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
