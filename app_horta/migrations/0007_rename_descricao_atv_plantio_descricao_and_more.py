# Generated by Django 5.1.2 on 2024-11-03 22:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_horta', '0006_solicitacaoacesso'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantio',
            old_name='descricao_atv',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='plantio',
            name='ultima_atv',
        ),
        migrations.AddField(
            model_name='plantio',
            name='horta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_horta.horta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantio',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plantio',
            name='dt_plantio',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]