# Generated by Django 4.2.11 on 2024-04-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_info', '0003_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(default='https://i.pinimg.com/736x/87/67/64/8767644bc68a14c50addf8cb2de8c59e.jpg', max_length=255),
        ),
    ]
