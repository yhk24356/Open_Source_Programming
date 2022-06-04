from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html')

def cold_medicine(request):
    return render(request, 'cold_medicine.html')

def back_pain_medicine(request):
    return render(request, 'back_pain_medicine.html')

def headache_medicine(request):
    return render(request, 'headache_medicine.html')

def muscle_pain_medicine(request):
    return render(request, 'muscle_pain_medicine.html')

def stomachache_medicine(request):
    return render(request, 'stomachache_medicine.html')

def toothache_medicine(request):
    return render(request, 'toothache_medicine.html')