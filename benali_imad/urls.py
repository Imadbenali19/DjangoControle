from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
#patient's urls

    path('patient/', views.indexP),
    path('patient/<int:id>', views.detailsP),

    path('addPatientForm/', views.createPatientForm),
    path('patient/edit/<int:id>', views.updatePatientForm),
    path('patient/delete/<int:id>', views.deleteP),

#medecin's urls

    path('medecin/', views.indexM),
    path('medecin/<int:id>', views.detailsM),

    path('addMedecinForm/', views.createMedecinForm),
    path('medecin/edit/<int:id>', views.updateMedecinForm),
    path('medecin/delete/<int:id>', views.deleteM),

#rendezVous's urls

    path('rendezVous/', views.indexR),
    path('rendezVous/<int:id>', views.detailsR),

    path('addRendezVousForm/', views.createRendezVousForm),
    path('rendezVous/edit/<int:id>', views.updateRendezVousForm),
    path('rendezVous/delete/<int:id>', views.deleteR),

#Search patient
    path('searchPatientByName/', views.searchPatientTraitement),


]