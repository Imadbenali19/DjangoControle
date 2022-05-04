from datetime import datetime

from django.shortcuts import render, redirect
from .models import Patient,Medecin,RendezVous
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from .forms import SearchPatientForm,PatientForm,MedecinForm,RendezVousForm

def index(request):
    return render(request, 'index.html',{'hi': 'jj'})


############################################
#Patient

#la liste des patients
def indexP(request):
    if 'search' in request.GET:
        search=request.GET['search']
        patients = Patient.objects.filter(nom__contains=search)

    else:
        patients = Patient.objects.all()

    #pagination
    paginator=Paginator(patients,10)
    page_number=request.GET.get('page',1)

    patie=paginator.get_page(page_number)

    nums= "a" * patie.paginator.num_pages
    patients=paginator.get_page(page_number)
    title = 'liste des patients'
    context = {'patients': patients,'nums':nums}
    return render(request, 'patient/index.html', context)


# pour afficher les détail d'un patient
def detailsP(request, id):
    patient = Patient.objects.get(id=id)
    context = {'patient': patient}
    return render(request, 'patient/details.html', context)

#Supprimer un patient
def deleteP(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return redirect("/patient")
    patient.delete()
    return redirect("/patient")

#Ajouter un patient
def createPatientForm(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patient')
    context={'form':form}
    return render(request,'formulaires/AddForm.html',context)

#Modifier un patient
def updatePatientForm(request,id):
    patient = Patient.objects.get(id=id)
    form=PatientForm(instance=patient)
    if request.method=='POST':
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/patient')
    context={'form':form}
    return render(request,'formulaires/AddForm.html',context)





############################################
#Medecin

#la liste des medecins
def indexM(request):
    if 'search' in request.GET:
        search=request.GET['search']
        medecins = Medecin.objects.filter(nom__contains=search)

    else:
        medecins = Medecin.objects.all()

    #pagination
    paginator=Paginator(medecins,10)
    page_number=request.GET.get('page',1)

    patie=paginator.get_page(page_number)

    nums= "a" * patie.paginator.num_pages
    medecins=paginator.get_page(page_number)
    title = 'liste des medecins'
    context = {'medecins': medecins,'nums':nums}
    return render(request, 'medecin/index.html', context)


# pour afficher les détail d'un medecin
def detailsM(request, id):
    medecin = Medecin.objects.get(id=id)
    context = {'medecin': medecin}
    return render(request, 'medecin/details.html', context)

#Supprimer un medecin
def deleteM(request, id):
    try:
        medecin = Medecin.objects.get(id=id)
    except Medecin.DoesNotExist:
        return redirect("/medecin")
    medecin.delete()
    return redirect("/medecin")

#Ajouter un medecin
def createMedecinForm(request):
    form=MedecinForm()
    if request.method=='POST':
        form=MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medecin')
    context={'form':form}
    return render(request,'formulaires/AddFormM.html',context)


#Modifier un médecin
def updateMedecinForm(request,id):
    medecin = Medecin.objects.get(id=id)
    form=MedecinForm(instance=medecin)
    if request.method=='POST':
        form=MedecinForm(request.POST,instance=medecin)
        if form.is_valid():
            form.save()
            return redirect('/medecin')
    context={'form':form}
    return render(request,'formulaires/AddFormM.html',context)



############################################
#Rendez Vous

#la liste des rendez-vous
def indexR(request):
    if 'search' in request.GET:
        search=request.GET['search']

        try :
            n=Patient.objects.get(nom=search).id
        except ObjectDoesNotExist :
            rendezVouss=RendezVous.objects.filter(date='1666-01-01')
        else:
            rendezVouss=RendezVous.objects.filter(patient_id=n)

    else:
        rendezVouss = RendezVous.objects.all()

    # pagination
    paginator = Paginator(rendezVouss, 10)
    page_number = request.GET.get('page', 1)

    patie = paginator.get_page(page_number)

    nums = "a" * patie.paginator.num_pages
    rendezVouss = paginator.get_page(page_number)
    title = 'liste des rendez-vous'

    context = {'rendezVouss': rendezVouss,'nums':nums}
    return render(request, 'rendezVous/index.html', context)


# pour afficher les détail d'un rendez-vous
def detailsR(request, id):
    try:
        rendezVous = RendezVous.objects.get(id=id)
    except ObjectDoesNotExist:
        context = {'rendezVous': None}
    else:
        context = {'rendezVous': rendezVous}


    return render(request, 'rendezVous/details.html', context)


#Supprimer un rendez-vous
def deleteR(request, id):
    try:
        rendezVous = RendezVous.objects.get(id=id)
    except RendezVous.DoesNotExist:
        return redirect("/rendezVous")
    rendezVous.delete()
    return redirect("/rendezVous")

#Ajouter un rendez-vous
def createRendezVousForm(request):
    form=RendezVousForm()
    if request.method=='POST':
        form=RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rendezVous')
    context={'form':form}
    return render(request,'formulaires/AddFormR.html',context)


#Modifier un rendez-vous
def updateRendezVousForm(request,id):
    rendezVous = RendezVous.objects.get(id=id)
    form=RendezVousForm(instance=rendezVous)
    if request.method=='POST':
        form=RendezVousForm(request.POST,instance=rendezVous)
        if form.is_valid():
            form.save()
            return redirect('/rendezVous')
    context={'form':form}
    return render(request,'formulaires/AddFormR.html',context)




#######################################################################

#Formulaire générale pour la recherche d'un patient par nom :

def searchPatientTraitement(request):
    form = SearchPatientForm()
    if request.method=='POST':
        form = SearchPatientForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            try:
                p = Patient.objects.get(nom=nom)
            except ObjectDoesNotExist:
                context = {'data': None,'form':form}
            else:
                context = {'data': p,'form':form}
                return render(request, 'formulaires/formTemplate.html', context)

    context={'form':form}
    return render(request, 'formulaires/formTemplate.html', context)