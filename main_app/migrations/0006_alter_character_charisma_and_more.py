# Generated by Django 4.2.6 on 2023-10-18 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_character_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(),
        ),
    ]
