# Generated by Django 3.2.12 on 2023-10-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(choices=[('Harpers', 'Harpers'), ('Order of the Gauntlet', 'Order of the Gauntlet'), ('Emerald Enclave', 'Emerald Enclave'), ('Lords Alliance', 'Lords Alliance'), ('Zhentarim', 'Zhentarim')], default='Harpers', max_length=25),
        ),
    ]