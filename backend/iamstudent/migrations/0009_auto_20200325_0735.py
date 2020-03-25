# Generated by Django 3.0.4 on 2020-03-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0008_merge_20200325_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ausbildung_typ_fsj',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='ausbildung_typ_hebamme',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='ausbildung_typ_physio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='ausbildung_typ_physio_abschnitt',
            field=models.IntegerField(choices=[(0, 'Keine Angabe'), (1, '1. Jahr'), (2, '2. Jahr'), (3, '3. Jahr'), (4, 'Berufstätig')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_arzt_typ',
            field=models.IntegerField(choices=[(0, 'Keine Angabe'), (1, 'Anästhesie'), (2, 'Chirurgie'), (3, 'Innere Medizin'), (4, 'Intensivstation'), (5, 'Notaufnahme')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_medstud_abschnitt',
            field=models.IntegerField(blank=True, choices=[(0, 'Keine Angabe'), (1, 'Vorklinischer Teil (1.-5. Semester)'), (2, 'Klinischer Teil (6.-10. Semester)'), (3, 'Praktisches Jahr')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_mfa_abschnitt',
            field=models.IntegerField(choices=[(0, 'Keine Angabe'), (1, '1. Jahr'), (2, '2. Jahr'), (3, '3. Jahr'), (4, 'Berufstätig')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_mta_abschnitt',
            field=models.IntegerField(choices=[(0, 'Keine Angabe'), (1, '1. Jahr'), (2, '2. Jahr'), (3, '3. Jahr'), (4, 'Berufstätig')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_mtla_abschnitt',
            field=models.IntegerField(choices=[(0, 'Keine Angabe'), (1, '1. Jahr'), (2, '2. Jahr'), (3, '3. Jahr'), (4, 'Berufstätig')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_notfallsani_abschnitt',
            field=models.IntegerField(choices=[(0, 'Keine Angabe'), (1, '1. Jahr'), (2, '2. Jahr'), (4, 'Berufstätig')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_zahni_abschnitt',
            field=models.IntegerField(blank=True, choices=[(0, 'Keine Angabe'), (1, 'Vorklinischer Teil'), (2, 'Klinischer Teil')], default=0),
        ),
    ]
