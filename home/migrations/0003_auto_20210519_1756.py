# Generated by Django 3.1.7 on 2021-05-19 17:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(blank=True, max_length=254, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Treats',
            },
        ),
        migrations.AddField(
            model_name='drink',
            name='category',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
