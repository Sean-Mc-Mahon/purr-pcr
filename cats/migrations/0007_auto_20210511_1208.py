# Generated by Django 3.1.7 on 2021-05-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0006_auto_20210511_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='status',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='sex',
            name='sex',
            field=models.CharField(help_text='Ready to be adopted etc...', max_length=254),
        ),
    ]
