# Generated by Django 4.2.11 on 2024-04-18 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0002_remove_selling_business_business_details_and_more'),
        ('prods_servs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='businesses.business'),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
