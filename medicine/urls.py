from django.urls import path
from . import views

urlpatterns = [
    path('cold_medicine/', views.cold_medicine, name='cold_medicine'),
    path('back_pain_medicine/', views.back_pain_medicine, name='back_pain_medicine'),
    path('headache_medicine/', views.headache_medicine, name='headache_medicine'),
    path('muscle_pain_medicine/', views.muscle_pain_medicine, name='muscle_pain_medicine'),
    path('stomachache_medicine/', views.stomachache_medicine, name='stomachache_medicine'),
    path('toothache_medicine/', views.toothache_medicine, name='toothache_medicine'),
]