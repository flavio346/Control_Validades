# Generated by Django 2.1.7 on 2020-04-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Validades', '0003_auto_20200424_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='Fornecedor',
            field=models.CharField(max_length=30),
        ),
    ]
