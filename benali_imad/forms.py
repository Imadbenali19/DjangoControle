from django import forms
from .models import Patient,Medecin,RendezVous

#Formulaire de recherche d'un patient par nom
class SearchPatientForm(forms.Form) :
    nom=forms.CharField()

#Fomulaire de patient
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"
        widgets = {'dateNaisse': forms.DateInput(attrs={'class':'form-control','type': 'date'}), }

#Formulaire de medecin
class MedecinForm(forms.ModelForm):
    class Meta:
        model=Medecin
        fields="__all__"

#Formulaire de rendez-vous
class RendezVousForm(forms.ModelForm):
    class Meta:
        model=RendezVous
        fields="__all__"
        widgets = {'date': forms.DateInput(attrs={'class':'form-control','type': 'date'}), }