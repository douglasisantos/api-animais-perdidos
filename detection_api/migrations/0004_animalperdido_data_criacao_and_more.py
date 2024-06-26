# Generated by Django 5.0.2 on 2024-03-21 18:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection_api', '0003_animalperdido_endereco_alter_animalperdido_raca'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalperdido',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='animalperdido',
            name='descricao_objetos',
            field=models.CharField(default='Descrição não fornecida', max_length=100),
        ),
        migrations.AlterField(
            model_name='animalperdido',
            name='foto',
            field=models.ImageField(upload_to='animais/'),
        ),
        migrations.AlterField(
            model_name='animalperdido',
            name='raca',
            field=models.CharField(max_length=100),
        ),
    ]
