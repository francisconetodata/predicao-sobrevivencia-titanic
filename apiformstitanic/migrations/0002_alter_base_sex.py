# Generated by Django 4.0.5 on 2022-06-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiformstitanic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10, verbose_name='Sexo'),
        ),
    ]
