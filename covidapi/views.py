from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from covidapi.api import CovidAPI
from covidapi.forms import StateForm



@login_required
def covid_cases(request):
    state = ''
    context = {}
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
    else:
        form = StateForm()
        
    api_data = CovidAPI().request(state)
    
    if 'error' in api_data:
        messages.add_message(
            request, messages.ERROR, api_data['error'])
        context['object_list'] = api_data
    else:
        context['object_list'] = api_data
    
    context['form']= form

    return render(request, 'covid_cases_list.html', context)