# Generated by Django 4.1.7 on 2023-06-06 01:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('validade', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('informacoes', models.TextField()),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('idade', models.IntegerField()),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.funcao')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAtividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ordem_servico', models.IntegerField()),
                ('data_registro', models.DateField(auto_now_add=True)),
                ('turno_atual', models.CharField(max_length=100)),
                ('inspecao_equipamentos', models.TextField()),
                ('observacao_inspecao', models.TextField()),
                ('hora_inicial_evento', models.DateTimeField()),
                ('hora_final_evento', models.DateTimeField()),
                ('visitas', models.TextField()),
                ('manobras', models.TextField()),
                ('ronda_interna', models.BooleanField()),
                ('ronda_externa', models.BooleanField()),
                ('ronda', models.TextField()),
                ('imagens_videos', models.FileField(upload_to='registro/uploads/%Y-%m-%d')),
                ('evento_automatico', models.BooleanField(default=False)),
                ('Equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.equipamento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.funcionario')),
            ],
        ),
    ]
