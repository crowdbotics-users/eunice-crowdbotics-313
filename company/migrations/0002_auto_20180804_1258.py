# Generated by Django 2.1 on 2018-08-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='TIMESTAMP',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
