# Generated by Django 3.2.13 on 2022-08-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.IntegerField(default=100),
        ),
    ]
