# Generated by Django 4.2.11 on 2024-04-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_info', '0002_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
