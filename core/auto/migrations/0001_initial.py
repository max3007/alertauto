# Generated by Django 3.2.15 on 2023-02-15 22:07

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
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stato', models.CharField(choices=[('IN', 'In Circolazione'), ('RT', 'Rottamata'), ('VE', 'Venduta'), ('RU', 'Rubata'), ('FE', 'Ferma')], default='IN', max_length=2)),
                ('tipo', models.CharField(choices=[('AV', 'Autovettura'), ('MV', 'Motovettura')], default='AV', max_length=2)),
                ('car_model', models.CharField(max_length=100, verbose_name='Modello Auto')),
                ('targa', models.CharField(max_length=100, unique=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('image_main', models.ImageField(blank=True, null=True, upload_to='alertauto/', verbose_name='Immagine Auto')),
                ('image_thumb', models.ImageField(blank=True, null=True, upload_to='alertauto/')),
                ('file', models.FileField(blank=True, null=True, upload_to='documenti_auto', verbose_name='File Auto')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note Auto')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proprietario', to=settings.AUTH_USER_MODEL, verbose_name='proprietario')),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Auto',
            },
        ),
        migrations.CreateModel(
            name='DocumentoAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('numero', models.CharField(max_length=100, verbose_name='Numero')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note Documento')),
                ('data_documento', models.DateField(blank=True, null=True)),
                ('data_scadenza', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='documenti_auto', verbose_name='File Documento')),
                ('senza_scadenza', models.BooleanField(default=False, verbose_name='Senza Scadenza')),
                ('controllo_scadenza', models.BooleanField(default=True, verbose_name='Controlo Scadenza')),
                ('scaduto', models.BooleanField(default=False, verbose_name='Documento Scaduto')),
                ('archiviato', models.BooleanField(default=False, verbose_name='Documento Archiviato')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documenti', to='auto.auto')),
            ],
        ),
    ]