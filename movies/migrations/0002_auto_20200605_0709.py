# Generated by Django 3.0.7 on 2020-06-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpaa_rating',
            name='type',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG13', 'PG13'), ('R', 'R'), ('NC-17', 'NC-17'), ('NC16', 'NC16'), ('M18', 'M18'), ('R21', 'R21'), ('M', 'M'), ('M18', 'M18')], max_length=5),
        ),
    ]
