# Generated by Django 3.0.4 on 2020-03-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Validades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='Produto',
            field=models.CharField(max_length=40),
        ),
    ]
