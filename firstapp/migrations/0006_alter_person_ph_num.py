# Generated by Django 4.1.3 on 2022-11-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_remove_person_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ph_num',
            field=models.IntegerField(max_length=10),
        ),
    ]
