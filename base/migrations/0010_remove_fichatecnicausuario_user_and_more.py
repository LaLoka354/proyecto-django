# Generated by Django 5.0.1 on 2024-01-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_fichatecnicausuario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichatecnicausuario',
            name='user',
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='birth_place',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='conflictos_embarazo',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='diagnosticos',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='forma_nacimiento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='marital_status',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='meses_gestacion',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='motivo_consulta',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='n_hijo',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='otros_hechos_embarazo',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='pregunta_1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='pregunta_2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fichatecnicausuario',
            name='pregunta_3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fichatecnicausuario',
            name='birthday',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='infousuario',
            name='birthday',
            field=models.CharField(max_length=8),
        ),
    ]