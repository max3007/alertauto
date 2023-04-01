from core.common.form_widgets import CustomFileInput, CustomCarPhotoInput
from django import forms
from .models import Auto, DocumentoAuto
import re


class AutoForm(forms.ModelForm):

    class Meta:
        model = Auto
        fields = ['tipo', 'stato', 'marca', 'data_immatricolazione',
                  'car_model', 'carburante', 'targa', 'note', 'image_main', 'file']
        widgets = {
            "image_main": CustomCarPhotoInput(
                attrs={"class": "form-control form-file-input", "max_file_size": "5"}
            ),
            "file": CustomFileInput(
                attrs={"class": "form-control form-file-input", "max_file_size": "5"}
            ),
            "data_immatricolazione": forms.DateInput(
                format=("%d/%m/%Y"), attrs={"class": "form-control", "type": "date"}
            ),
        }

    def clean_targa(self):
        targa = self.cleaned_data['targa'].replace(" ", "").upper()
        tipo = self.cleaned_data['tipo']
        if tipo == 'AV':
            if not re.match(r'^[A-Z]{2}\d{3}[A-Z]{2}$', targa):
                raise forms.ValidationError("La targa non è valida")
        if tipo == 'MV':
            if not re.match(r'^[A-Z]{2}\d{5}$', targa):
                raise forms.ValidationError("La targa non è valida")
        if tipo == 'CM':
            if not re.match(r'^[2-9BCDFGHJKLMNPRTSUVWXYZ23456789]{6}$', targa):
                raise forms.ValidationError("La targa non è valida")
        self.cleaned_data['targa'] = targa
        return targa


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = DocumentoAuto
        fields = ['nome', 'numero', 'note', 'data_documento',
                  'data_scadenza', 'file', 'controllo_scadenza', 'archiviato']
        widgets = {
            "file": CustomFileInput(
                attrs={"class": "form-control form-file-input", "max_file_size": "1", "image_placeholder": "image", }
            ),
            "data_documento": forms.DateInput(
                format=("%d/%m/%Y"), attrs={"class": "form-control", "type": "date"}
            ),
            "data_scadenza": forms.DateInput(
                format=("%d/%m/%Y"), attrs={"class": "form-control", "type": "date"}
            ),
        }
