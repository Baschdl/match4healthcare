# from django.forms import *
from django import forms
from apps.iamstudent.models import Student, EmailToSend, AUSBILDUNGS_TYPEN, AUSBILDUNGS_IDS
from django.db import models
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Div, HTML
from crispy_forms.bootstrap import InlineRadios
from apps.iamstudent.custom_crispy import RadioButtons
from apps.accounts.models import User

import logging

form_labels = {
    'uuid': _('Writer'),
    'registration_date': _('Writer'),

    'name_first': _('Vorname'),
    'name_last': _('Nachname'),
    'phone_number': _('Telefonnummer'),

    'plz': _('Postleitzahl'),
    'countrycode': _('Land'),
    'email': _('Email'),

    'availability_start': _('Ich bin verfügbar ab'),
    'braucht_bezahlung': _('Ich benötige eine Vergütung'),

    # Form Labels for qualifications
    'ausbildung_typ_pflege': _('Pflege <em>(melde Dich auch bei <a href="https://pflegereserve.de/#/login">Pflegereserve</a>)</em>'),
    'ausbildung_typ_pflege_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_physio': _('Physiotherapieauszubildende*r'),
    'ausbildung_typ_physio_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_hebamme': _('Entbindungshelfer*in'),
    'ausbildung_typ_fsj': _('FSJ im Gesundheitswesen'),
    'ausbildung_typ_arzt': _('Arzt/Ärztin'),
    'ausbildung_typ_arzt_typ': _('Fachbereich'),
    'ausbildung_typ_arzt_sonstige': _('Sonstige:'),
    'ausbildung_typ_medstud': _('Medizinstudent*in'),
    'ausbildung_typ_medstud_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_medstud_farmulaturen_anaesthesie': _('Famulatur Anästhesie'),
    'ausbildung_typ_medstud_famulaturen_chirurgie': _('Famulatur Chirurgie'),
    'ausbildung_typ_medstud_famulaturen_innere': _('Famulatur Innere'),
    'ausbildung_typ_medstud_famulaturen_intensiv': _('Famulatur Intensivmedizin'),
    'ausbildung_typ_medstud_famulaturen_notaufnahme': _('Famulatur Notaufnahme'),
    'ausbildung_typ_medstud_anerkennung_noetig': _(
        'Eine Anerkennung als Teil eines Studienabschnitts (Pflegepraktikum/Famulatur) ist wichtig'),
    'ausbildung_typ_mfa': _('Medizinische/r Fachangestellte*r'),
    'ausbildung_typ_mfa_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_mtla': _('Medizinisch-technische/r Laboratoriumsassistent*in'),
    'ausbildung_typ_mtla_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_mta': _('Medizinisch-technische/r Assistent*in'),
    'ausbildung_typ_mta_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_notfallsani': _('Notfallsanitäter*in/Rettungsassistent*in'),
    'ausbildung_typ_notfallsani_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_sani': _('Rettungssanitäter*in/Rettungshelfer*in'),
    'ausbildung_typ_zahni': _('Zahnmedizinstudent*in'),
    'ausbildung_typ_zahni_abschnitt': _('Ausbildungsabschnitt'),
    'ausbildung_typ_kinderbetreung': _('Kinderbetreuer*in'),
    'ausbildung_typ_kinderbetreung_ausgebildet': _('Abgeschlossene Ausbildung'),
    'ausbildung_typ_kinderbetreung_vorerfahrung': _('Lediglich Erfahrungen'),
    'ausbildung_typ_sonstige': _('Sonstige'),
    'ausbildung_typ_sonstige_eintragen': _('Bitte die Qualifikationen hier eintragen'),
    'datenschutz_zugestimmt': _('Hiermit akzeptiere ich die <a href="/dataprotection/">Datenschutzbedingungen</a>.'),
    'einwilligung_datenweitergabe': _(
        'Ich bestätige, dass meine Angaben korrekt sind und ich der Institution meinen Ausbildungsstand nachweisen kann. Mit der Weitergabe meiner Kontaktdaten an die Institutionen bin ich einverstanden.'),
    'wunsch_ort_arzt': _('Arztpraxis/Ordination/MVZ'),
    'wunsch_ort_gesundheitsamt': _('Gesundheitsamt und sonstige Einrichtungen'),
    'wunsch_ort_krankenhaus': _('Klinikum/Spital'),
    'wunsch_ort_pflege': _('Pflegeeinrichtungen'),
    'wunsch_ort_rettungsdienst': _('Rettungsdienst'),
    'wunsch_ort_labor': _('Labor'),
    'zeitliche_verfuegbarkeit': _('Zeitliche Verfügbarkeit, bis zu'),
}
fields_for_button_group = ['ausbildung_typ_arzt_typ',
'ausbildung_typ_pflege_abschnitt',
                           'ausbildung_typ_physio_abschnitt',
                           'ausbildung_typ_medstud_abschnitt',
                           'ausbildung_typ_mfa_abschnitt',
                           'ausbildung_typ_mtla_abschnitt',
                           'ausbildung_typ_mta_abschnitt',
                           'ausbildung_typ_notfallsani_abschnitt',
                           'ausbildung_typ_zahni_abschnitt']


def button_group(field):
    if 'empty' in field:
        return Column()
    if field in fields_for_button_group:
        return ButtonGroup(field)
    return field


def ButtonGroup(field):
    return RadioButtons(field, option_label_class="btn btn-sm btn-light",
                        template='input_buttongroup-any_indicator.html')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['uuid', 'registration_date', 'user']
        labels = form_labels
        help_texts = {
            'email': _('Über diese Emailadresse dürfen dich medizinische Einrichtungen kontaktieren'),
            'countrycode': _('Bitte wähle ein Land aus'),
            'plz': _('bevorzugter Einsatzort als Postleitzahl'),
           # 'wunsch_ort_gesundheitsamt': _('Hotline, Teststation etc.')
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False

        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.layout = Layout(
            Row(
                Column('name_first', css_class='form-group col-md-6 mb-0'),
                Column('name_last', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            HTML("<h2>{}</h2>".format(_("Einsatz"))),
            Row(
                Column('plz', css_class='form-group col-md-4 mb-0'),
                Column('countrycode', css_class='form-group col-md-4 mb-0'),
                Column('umkreis', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('availability_start', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            HTML("<h5>{}</h5>".format(_("Wunscheinsatzort"))),
            Row(
                Column('wunsch_ort_arzt', css_class='form-group col-md-6 mb-0'),
                Column('wunsch_ort_gesundheitsamt', css_class='form-group col-md-6 mb-0'),
                Column('wunsch_ort_krankenhaus', css_class='form-group col-md-6 mb-0'),
                Column('wunsch_ort_pflege', css_class='form-group col-md-6 mb-0'),
                Column('wunsch_ort_rettungsdienst', css_class='form-group col-md-6 mb-0'),
                Column('wunsch_ort_labor', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('braucht_bezahlung', css_class='form-group col-md-6 mb-0'),
                Column('zeitliche_verfuegbarkeit', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Div(
                HTML("<h2>{}</h2>".format(_("Berufsausbildung"))),
                Row(*[Column('ausbildung_typ_%s' % k.lower(), css_class='ausbildung-checkbox form-group col-md-6 mb-0',
                             css_id='ausbildung-checkbox-%s' % AUSBILDUNGS_IDS[k]) for k in
                      AUSBILDUNGS_TYPEN.keys()]),
                css_id='div-berufsausbildung-dropdown',
            ),
            *[
                Div(
                    HTML("<h4>{}</h4>".format(_(form_labels['ausbildung_typ_%s' % ausbildungstyp.lower()]))),
                    Row(*[
                        Column(button_group('ausbildung_typ_%s_%s' % (ausbildungstyp.lower(), f.lower())),
                               css_class='form-group col-md-6 mb-0', css_id=f.replace('_', '-'))
                        for f in felder.keys()
                    ]), css_id='div-ausbildung-%s' % AUSBILDUNGS_IDS[ausbildungstyp]
                    , css_class='hidden ausbildung-addon'
                )
                for ausbildungstyp, felder in AUSBILDUNGS_TYPEN.items() if len(felder) != 0
            ]
            ,
            HTML('<hr>'),
            HTML('<p class="text-left">'),
            'datenschutz_zugestimmt',
            HTML("</p>"),
            HTML('<p class="text-left">'),
            'einwilligung_datenweitergabe',
            HTML("</p>"),
            HTML('<div class="registration_disclaimer">{}</div>'.format(_('Die Vermittlung erfolgt unentgeltlich. Mir ist bewusst, dass die Ausgestaltung des Verhältnisses zur zu vermittelnden Institution allein mich und die entsprechende Institution betrifft. Insbesondere Art und Umfang der Arbeit, eine etwaige Vergütung und vergleichbares betreffen nur mich und die entsprechende Institution. Eine Haftung des Vermittlers ist ausgeschlossen.'))),          
            Submit('submit', _('Registriere mich'), css_class='btn blue text-white btn-md'),          
        )

        logging.debug(self.helper.layout)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Diese Email ist bereits vergeben"))
        return email


class StudentFormAndMail(StudentForm):
    email = forms.EmailField()


class EmailForm(forms.Form):
    student_id = forms.CharField(max_length=100)
    contact_adress = forms.EmailField()


class StudentFormEditProfile(StudentForm):
    def __init__(self, *args, **kwargs):
        super(StudentFormEditProfile, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Row(
                Column('name_first', css_class='form-group col-md-6 mb-0'),
                Column('name_last', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('plz', css_class='form-group col-md-6 mb-0'),
                Column('countrycode', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('availability_start', css_class='form-group col-md-6 mb-0'),
                #Column('semester', css_class='form-group col-md-4 mb-0'),
                #Column('immatrikuliert', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('braucht_bezahlung', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML("<h2>{}</h2>".format(_("Berufsausbildung"))),
            # TODO: alle neuen felder hier auch hinzufügen!!!!!
                        Submit('submit', _('Daten aktualisieren',), css_class='btn blue text-white btn-md'),
                  )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Diese Email ist bereits vergeben"))
        return email


class EmailToSendForm(forms.ModelForm):
    class Meta:
        model = EmailToSend
        fields = ['subject', 'message']
        labels = {'subject': _('Betreff'),
                  'message': _('Nachrichtentext')}
        help_texts = {
            'message': _('Hier soll Eure Stellenanzeige stehen, editiert den Text.')
        }
