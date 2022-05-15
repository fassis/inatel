from django.urls import path

from covidapi import views

app_name = 'covidapi'

urlpatterns = [
    path('cases', views.covid_cases, name='covid_cases'),
]