from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cold_medicine(request):
    return render(request, 'medicine/cold_medicine.html')

def back_pain_medicine(request):
    return render(request, 'medicine/back_pain_medicine.html')

def headache_medicine(request):
    return render(request, 'medicine/headache_medicine.html')

def muscle_pain_medicine(request):
    return render(request, 'medicine/muscle_pain_medicine.html')

def stomachache_medicine(request):
    return render(request, 'medicine/stomachache_medicine.html')

def toothache_medicine(request):
    return render(request, 'medicine/toothache_medicine.html')