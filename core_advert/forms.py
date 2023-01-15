from django import forms
from .models import (Inkoranya,Ubukwe,Imbyino,Ibikoresho,Ubuhinzi,Indamukanyo,
Amasano,Ikibonezamvugo,Umurage,Hugura)

class InkoranyaForm(forms.ModelForm):
    class Meta:
        model=Inkoranya
        fields=('name','description')

class UbukweForm(forms.ModelForm):
    class Meta:
        model=Ubukwe
        fields=('name','description')

class ImbyinoForm(forms.ModelForm):
    class Meta:
        model=Imbyino
        fields=('name','cover','description')

class IbikoreshoForm(forms.ModelForm):
    class Meta:
        model=Ibikoresho
        fields=('name','image','description')

class UbuhinziForm(forms.ModelForm):
    class Meta:
        model=Ubuhinzi
        fields=('name','description')

class IndamukanyoForm(forms.ModelForm):
    class Meta:
        model=Indamukanyo
        fields=('name','description')

class AmasanoForm(forms.ModelForm):
    class Meta:
        model=Amasano
        fields=('name','description')

class IkibonezamvugoForm(forms.ModelForm):
    class Meta:
        model=Ikibonezamvugo
        fields=('name','cover','description')

class UmurageForm(forms.ModelForm):
    class Meta:
        model=Umurage
        fields=('name','description')

class HuguraForm(forms.ModelForm):
    class Meta:
        model=Hugura
        fields=('cover','name')

