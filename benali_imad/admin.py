from django.contrib import admin
from .models import Patient,Medecin,RendezVous

@admin.register(Patient)
class patientModelAdmin(admin.ModelAdmin):
    list_display = ('id','nom','prenom','dateNaisse','email')
    ordering = ('id',)
    list_filter = ('nom','dateNaisse')
    search_fields = ('nom','id','dateNaisse','email')

@admin.register(Medecin)
class medecinModelAdmin(admin.ModelAdmin):
    list_display = ('id','nom','prenom','specialite')
    ordering = ('id',)
    list_filter = ('nom','specialite')
    search_fields = ('nom','id','specialite')

@admin.register(RendezVous)
class rendezVousModelAdmin(admin.ModelAdmin):
    list_display = ('id','date','patient','medecin','annule')
    ordering = ('id',)
    list_filter = ('date','patient')
    search_fields = ('date','id','patient','medecin')