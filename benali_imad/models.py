from django.db import models
from datetime import date

#model Patient
class Patient(models.Model):
    nom=models.CharField(max_length=80)
    prenom=models.CharField(max_length=80)
    email=models.EmailField()
    dateNaisse=models.DateField()
    def __str__(self):
        return self.nom

#model Medecin
class Medecin(models.Model):
    nom=models.CharField(max_length=80)
    prenom=models.CharField(max_length=80)
    specialite=models.CharField(max_length=80)
    def __str__(self):
        return self.nom

#model Rendez vous
class RendezVous(models.Model):
    date=models.DateField()
    annule=models.BooleanField()
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    medecin=models.ForeignKey(Medecin,on_delete=models.CASCADE,null=True)


#Model Consultation
class Consultation(models.Model):
    TYPE = (('Presentielle','Presentielle'),('Distantielle','Distantielle'))
    description=models.CharField(max_length=80)
    traitementPrescrit=models.CharField(max_length=80)
    type=models.CharField(max_length=80,choices=TYPE)
    rendeVous=models.OneToOneField(RendezVous,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.description