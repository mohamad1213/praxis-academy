# Generated by Django 2.2 on 2020-09-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitra',
            name='alamat',
            field=models.CharField(max_length=255),
        ),
    ]
