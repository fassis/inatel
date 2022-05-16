import json
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib import messages
from rest_framework.renderers import JSONRenderer

from coreapp.models import HealthUnity, HealthUnityFile
from coreapp.forms import ImportHealthUnityForm
from coreapp.serializers import HealthUnitySerializer
from coreapp.utils import dataframe_from_file


@login_required
@csrf_exempt
@transaction.atomic
def health_unities_import(request):
    
    if request.method == 'POST':
        form = ImportHealthUnityForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            try:
                with transaction.atomic():
                    data = dataframe_from_file(file)
                    health_unity_file = HealthUnityFile.objects.create(file=file)
                    health_unity_file.save_data_frame(data)

                    messages.add_message(request, messages.SUCCESS,
                                         'Importação realizada com sucesso.')
            except Exception as err:
                messages.add_message(request, messages.ERROR, err)
    else:
        form = ImportHealthUnityForm()
    
    context = {'form':form}
    
    return render(request, 'app/ubs_import.html', context)


@login_required
def health_unity_file_list(request):
    unity_files = HealthUnityFile.objects.all().order_by('-created_at')
    context = {'unity_files': unity_files}

    return render(request, 'app/ubs_file_list.html', context )


@login_required
def health_unity_file_detail(request, health_unity_file_pk):
    unities_file = get_object_or_404(HealthUnityFile, pk=health_unity_file_pk)
    unities = HealthUnity.objects.filter(file=unities_file)
    serializer = HealthUnitySerializer(unities, many=True)
    unities_json = json.dumps(serializer.data)

    context = {
        'unities_file': unities_file,
        'unities': unities_json
    }

    return render(request, 'app/ubs_detail.html', context)

@login_required
def health_unity_list(request, health_unity_file_pk):
    unities_file = get_object_or_404(HealthUnityFile, pk=health_unity_file_pk)
    unities = HealthUnity.objects.filter(file=unities_file)
    
    context = {
        'object_list': unities,
        'title': 'Lista de Unidades Básicas de Saúde'
    }

    return render(request, 'app/generic_list.html', context )

@login_required
def health_unity_state_list(request, state):
    unities = HealthUnity.objects.filter(ibge_uf=state)
    
    context = {
        'object_list': unities,
        'title': 'Lista de {} Unidades Básicas de Saúde de {}'.format(len(unities), state)
    }

    return render(request, 'app/generic_list.html', context )

