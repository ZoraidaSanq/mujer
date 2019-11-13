# Generated by Django 2.1 on 2019-11-13 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isuso', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('num_pre_asig', models.PositiveIntegerField()),
                ('isorden', models.BooleanField(default=True)),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EncuestaMujer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isuso', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField(blank=True)),
                ('num_pre_asig', models.PositiveIntegerField()),
                ('num_pre_resuelta', models.PositiveIntegerField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='encuesta.Encuesta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Factorviolencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isuso', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('valori', models.PositiveIntegerField()),
                ('valord', models.PositiveIntegerField()),
                ('valora', models.PositiveIntegerField()),
                ('sumag', models.PositiveIntegerField()),
                ('resultado', models.CharField(max_length=60)),
                ('encuesta_mujer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='encuesta.EncuestaMujer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Likert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isuso', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('denominacion', models.CharField(max_length=60)),
                ('valor', models.PositiveIntegerField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='encuesta.Encuesta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mujer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isuso', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('ocupacion', models.CharField(max_length=40)),
                ('estadocivil', models.CharField(max_length=1)),
                ('nivel_educacion', models.CharField(max_length=60)),
                ('hijos', models.PositiveIntegerField()),
                ('edad', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isuso', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('pregunta', models.CharField(max_length=60)),
                ('orden', models.PositiveIntegerField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='encuesta.Encuesta')),
                ('likert', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='encuesta.Likert')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Preguntaresultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isuso', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('valor', models.PositiveIntegerField()),
                ('valor_denom', models.CharField(max_length=60)),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='encuesta.EncuestaMujer')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='encuesta.Pregunta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='encuestamujer',
            name='mujer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='encuesta.Mujer'),
        ),
    ]