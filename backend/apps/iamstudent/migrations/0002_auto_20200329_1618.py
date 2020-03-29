# Generated by Django 3.0.4 on 2020-03-29 16:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ineedstudent', '0001_initial'),
        ('iamstudent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationFilterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plz', models.CharField(max_length=5, null=True)),
                ('distance', models.IntegerField(default=0)),
                ('countrycode', models.CharField(choices=[('DE', 'Deutschland'), ('AT', 'Österreich')], default='DE', max_length=2)),
                ('uuid', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentListFilterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('registration_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('name', models.CharField(max_length=100)),
                ('ausbildung_typ_medstud', models.NullBooleanField(default=None)),
                ('ausbildung_typ_mfa', models.NullBooleanField(default=None)),
                ('ausbildung_typ_mtla', models.NullBooleanField(default=None)),
                ('ausbildung_typ_mta', models.NullBooleanField(default=None)),
                ('ausbildung_typ_notfallsani', models.NullBooleanField(default=None)),
                ('ausbildung_typ_pflege', models.NullBooleanField(default=None)),
                ('ausbildung_typ_sani', models.NullBooleanField(default=None)),
                ('ausbildung_typ_hebamme', models.NullBooleanField(default=None)),
                ('ausbildung_typ_fsj', models.NullBooleanField(default=None)),
                ('ausbildung_typ_zahni', models.NullBooleanField(default=None)),
                ('ausbildung_typ_physio', models.NullBooleanField(default=None)),
                ('ausbildung_typ_kinderbetreung', models.NullBooleanField(default=None)),
                ('ausbildung_typ_medstud_famulaturen_anaesthesie', models.NullBooleanField(default=None)),
                ('ausbildung_typ_medstud_famulaturen_chirurgie', models.NullBooleanField(default=None)),
                ('ausbildung_typ_medstud_famulaturen_innere', models.NullBooleanField(default=None)),
                ('ausbildung_typ_medstud_famulaturen_intensiv', models.NullBooleanField(default=None)),
                ('ausbildung_typ_medstud_famulaturen_notaufnahme', models.NullBooleanField(default=None)),
                ('ausbildung_typ_medstud_anerkennung_noetig', models.NullBooleanField(default=None)),
                ('ausbildung_typ_kinderbetreung_ausgebildet_abschnitt', models.IntegerField(choices=[('', '---------'), (0, 'Keine Angabe'), (1, 'Lediglich Erfahrungen'), (2, 'Abgeschlossene Ausbildung')], default=0)),
                ('ausbildung_typ_medstud_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_medstud_abschnitt_x_lt', models.IntegerField(default=0)),
                ('ausbildung_typ_mfa_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_mfa_abschnitt_x_lt', models.IntegerField(default=0)),
                ('ausbildung_typ_mta_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_mta_abschnitt_x_lt', models.IntegerField(default=0)),
                ('ausbildung_typ_mtla_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_mtla_abschnitt_x_lt', models.IntegerField(default=0)),
                ('ausbildung_typ_notfallsani_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_notfallsani_abschnitt_x_lt', models.IntegerField(default=0)),
                ('ausbildung_typ_physio_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_physio_abschnitt_x_lt', models.IntegerField(default=0)),
                ('ausbildung_typ_pflege_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_pflege_abschnitt_x_lt', models.IntegerField(default=0)),
                ('ausbildung_typ_zahni_abschnitt_x_gt', models.IntegerField(default=0)),
                ('ausbildung_typ_zahni_abschnitt_x_lt', models.IntegerField(default=0)),
                ('braucht_bezahlung', models.IntegerField(choices=[('', 'wissen wir nicht'), (1, 'ja'), (2, 'nein')], default=0)),
                ('availability_start', models.DateField(default=datetime.datetime.now, null=True)),
                ('unterkunft_gewuenscht', models.IntegerField(choices=[('', 'wissen wir nicht'), (True, 'ja'), (False, 'nein')], default=0)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ineedstudent.Hospital')),
            ],
        ),
        migrations.DeleteModel(
            name='PersistenStudentFilterModel',
        ),
    ]