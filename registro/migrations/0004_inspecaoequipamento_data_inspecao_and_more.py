# Generated by Django 4.1.7 on 2023-06-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_remove_inspecaoequipamento_registro_atividades_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspecaoequipamento',
            name='data_inspecao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inspecaoequipamento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registroatividades',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
