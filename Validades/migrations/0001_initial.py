# Generated by Django 3.0.4 on 2020-03-26 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto', models.CharField(max_length=15)),
                ('Fornecedor', models.CharField(max_length=10)),
                ('Quantidade', models.IntegerField()),
                ('Data_do_Registro', models.DateField()),
                ('Validade', models.DateField()),
            ],
        ),
    ]
