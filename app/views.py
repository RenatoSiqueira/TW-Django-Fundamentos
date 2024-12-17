import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ClientForm

# Create your views here.


def horario_atual(request):
    horario_atual = datetime.datetime.now()
    # return HttpResponse(f'O horário atual é: {horario_atual}')
    return render(request, 'lista_horario.html', context={'horario_atual': horario_atual})


def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse('Cliente cadastrado com sucesso!')
        else:
            return HttpResponse('Formulário inválido!')
    form = ClientForm()
    return render(request, 'form_client.html', context={'form': form})
