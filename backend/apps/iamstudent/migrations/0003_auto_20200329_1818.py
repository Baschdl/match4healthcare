# Generated by Django 3.0.4 on 2020-03-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0002_auto_20200329_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_medstud_abschnitt',
            field=models.IntegerField(choices=[(0, 'Keine Angabe'), (1, 'Vorklinischer Teil'), (2, 'Klinischer Teil'), (3, 'Praktisches Jahr'), (4, 'Assistenzarzt'), (5, 'Facharzt')], default=0, null=True),
        ),
    ]
