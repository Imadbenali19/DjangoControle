# Generated by Django 4.0.4 on 2022-05-03 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80)),
                ('prenom', models.CharField(max_length=80)),
                ('specialite', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80)),
                ('prenom', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('dateNaisse', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('annule', models.BooleanField()),
                ('medecin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='benali_imad.medecin')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='benali_imad.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=80)),
                ('traitementPrescrit', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=80)),
                ('rendeVous', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='benali_imad.rendezvous')),
            ],
        ),
    ]