# Generated by Django 5.1.3 on 2024-12-01 23:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('ativo', models.BooleanField(default=True)),
                ('cep', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('engenheiro_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obras', to='users.engineerprofile')),
            ],
        ),
    ]