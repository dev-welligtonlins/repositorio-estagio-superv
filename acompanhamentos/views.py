from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Acompanhamentos, AcompanhamentoMonitores, AcompanhamentoTutores, AcompanhamentoInterpretes, AcompanhamentoDisciplinas
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import AcompanhamentosForm, AcoMonitoriasForm, AcoTutoriasForm, AcoInterpretacoesForm, AcoDisciplinasForm

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

#ALUNOS========================================================================================

def acoIndex(request):
    acompanhamentos = Acompanhamentos.objects.order_by('-aco_id')
    paginator = Paginator(acompanhamentos, 10)

    page = request.GET.get('p')
    acompanhamentos = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoIndex.html', {
        'acompanhamentos': acompanhamentos
    })

def adicionarAcompanhamento(request):
    submitted = False

    context = {}
    if request.POST:
        form = AcompanhamentosForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarAcompanhamento?submitted=True')
        else:
            form = AcompanhamentosForm()
            form.save()
            return HttpResponseRedirect('adicionarAcompanhamento?submitted=True')
    else:
        form = AcompanhamentosForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'acompanhamentos/adicionarAcompanhamento.html', context)

def acompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    try:
        monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_acompanhamento=acompanhamento)
    except:
        monitoria = None
    try:
        tutoria = get_object_or_404(AcompanhamentoTutores, AsTut_acompanhamento=acompanhamento)
    except:
        tutoria = None
    try:
        interpretacoes = AcompanhamentoInterpretes.objects.filter(AsInt_acompanhamento=acompanhamento)
    except:
        interpretacoes = None
    try:
        disciplinas = AcompanhamentoDisciplinas.objects.filter(AsDis_acompanhamento=acompanhamento)
    except:
        disciplinas = None

    return render(request, 'acompanhamentos/acompanhamento.html', {
        'acompanhamento': acompanhamento,
        'monitoria': monitoria,
        'tutoria': tutoria,
        'interpretacoes': interpretacoes,
        'disciplinas': disciplinas
    })

def atualizarAcompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)

    form = AcompanhamentosForm(request.POST or None, instance=acompanhamento)
    if form.is_valid():
        form.save()
        return redirect('acoIndex')

    return render(request, 'acompanhamentos/atualizarAcompanhamento.html', {
        'acompanhamento': acompanhamento,
        'form': form
    })

def buscarAcompanhamento(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
                Q(aco_semestre__icontains=searched) | Q(aco_aluno_pcd__alu_nome__icontains=searched)
            )
        else:
            acompanhamentos = None

        return render(request, 'acompanhamentos/buscarAcompanhamento.html', {
            'searched': searched,
            'acompanhamentos': acompanhamentos
        })
    else:
        return render(request, 'acompanhamentos/buscarAcompanhamento.html', {

        })

def deletarAcompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    acompanhamento.delete()
    return redirect('acoIndex')

#DISCIPLINAS===================================================================================

def acoDisIndex(request):
    disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id')
    paginator = Paginator(disciplinas, 10)

    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoDisIndex.html', {
        'disciplinas': disciplinas
    })

def adicionarDisciplina(request):
    submitted = False

    context = {}
    if request.POST:
        form = AcoDisciplinasForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarDisciplina?submitted=True')
        else:
            form = AcoDisciplinasForm()
            form.save()
            return HttpResponseRedirect('adicionarDisciplina?submitted=True')
    else:
        form = AcoDisciplinasForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'acompanhamentos/adicionarDisciplina.html', context)

def atualizarDisciplina(request, disciplina_id):
    disciplina = get_object_or_404(AcompanhamentoDisciplinas, AsDis_id=disciplina_id)

    form = AcoDisciplinasForm(request.POST or None, instance=disciplina)
    if form.is_valid():
        form.save()
        return redirect('acoDisIndex')

    return render(request, 'acompanhamentos/atualizarDisciplina.html', {
        'disciplina': disciplina,
        'form': form
    })

def buscarDisciplina(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            disciplinas = AcompanhamentoDisciplinas.objects.order_by('-AsDis_id').filter(
                Q(AsDis_disciplina__dis_nome__icontains=searched) |
                Q(AsDis_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched ) |
                Q(AsDis_acompanhamento__aco_semestre__icontains=searched)
            )
        else:
            disciplinas = None

        return render(request, 'acompanhamentos/buscarDisciplina.html', {
            'searched': searched,
            'disciplinas': disciplinas
        })
    else:
        return render(request, 'acompanhamentos/buscarDisciplina.html', {

        })

def deletarDisciplina(request, disciplina_id):
    disciplina = get_object_or_404(AcompanhamentoDisciplinas, AsDis_id=disciplina_id)
    disciplina.delete()
    return redirect('acoDisIndex')

#INTERPRETES===================================================================================

def acoIntIndex(request):
    interpretacoes = AcompanhamentoInterpretes.objects.order_by('-AsInt_id')
    paginator = Paginator(interpretacoes, 10)

    page = request.GET.get('p')
    interpretacoes = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoIntIndex.html', {
        'interpretacoes': interpretacoes
    })

def adicionarInterpretacao(request):
    submitted = False

    context = {}
    if request.POST:
        form = AcoInterpretacoesForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarInterpretacao?submitted=True')
        else:
            form = AcoInterpretacoesForm()
            form.save()
            return HttpResponseRedirect('adicionarInterpretacao?submitted=True')
    else:
        form = AcoInterpretacoesForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'acompanhamentos/adicionarInterpretacao.html', context)

def atualizarInterpretacao(request, interpretacao_id):
    interpretacao = get_object_or_404(AcompanhamentoInterpretes, AsInt_id=interpretacao_id)

    form = AcoInterpretacoesForm(request.POST or None, instance=interpretacao)
    if form.is_valid():
        form.save()
        return redirect('acoIntIndex')

    return render(request, 'acompanhamentos/atualizarInterpretacao.html', {
        'interpretacao': interpretacao,
        'form': form
    })

def buscarInterpretacao(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            interpretacoes = AcompanhamentoInterpretes.objects.order_by('-AsInt_id').filter(
                Q(AsInt_interprete__int_nome__icontains=searched) |
                Q(AsInt_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsInt_acompanhamento__aco_semestre__icontains=searched)
            )
        else:
            interpretacoes = None

        return render(request, 'acompanhamentos/buscarInterpretacao.html', {
            'searched': searched,
            'interpretacoes': interpretacoes
        })
    else:
        return render(request, 'acompanhamentos/buscarInterpretacao.html', {

        })

def deletarInterpretacao(request, interpretacao_id):
    interpretacao = get_object_or_404(AcompanhamentoInterpretes, AsInt_id=interpretacao_id)
    interpretacao.delete()
    return redirect('acoIntIndex')

#MONITORES=====================================================================================

def acoMonIndex(request):
    monitorias = AcompanhamentoMonitores.objects.order_by('-AsMon_id')
    paginator = Paginator(monitorias, 10)

    page = request.GET.get('p')
    monitorias = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoMonIndex.html', {
        'monitorias': monitorias
    })

def adicionarMonitoria(request):
    submitted = False

    context = {}
    if request.POST:
        form = AcoMonitoriasForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarMonitoria?submitted=True')
        else:
            form = AcoMonitoriasForm()
            form.save()
            return HttpResponseRedirect('adicionarMonitoria?submitted=True')
    else:
        form = AcoMonitoriasForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'acompanhamentos/adicionarMonitoria.html', context)

def atualizarMonitoria(request, monitoria_id):
    monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_id=monitoria_id)

    form = AcoMonitoriasForm(request.POST or None, instance=monitoria)
    if form.is_valid():
        form.save()
        return redirect('acoMonIndex')

    return render(request, 'acompanhamentos/atualizarMonitoria.html', {
        'monitoria': monitoria,
        'form': form
    })

def buscarMonitoria(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            monitorias = AcompanhamentoMonitores.objects.order_by('-AsMon_id').filter(
                Q(AsMon_monitor__mon_nome__icontains=searched) |
                Q(AsMon_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsMon_acompanhamento__aco_semestre__icontains=searched)
            )
        else:
            monitorias = None

        return render(request, 'acompanhamentos/buscarMonitoria.html', {
            'searched': searched,
            'monitorias': monitorias
        })
    else:
        return render(request, 'acompanhamentos/buscarMonitoria.html', {

        })

def deletarMonitoria(request, monitoria_id):
    monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_id=monitoria_id)
    monitoria.delete()
    return redirect('acoMonIndex')

#TUTORES=======================================================================================

def acoTutIndex(request):
    tutorias = AcompanhamentoTutores.objects.order_by('-AsTut_id')
    paginator = Paginator(tutorias, 10)

    page = request.GET.get('p')
    tutorias = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoTutIndex.html', {
        'tutorias': tutorias
    })

def adicionarTutoria(request):
    submitted = False

    context = {}
    if request.POST:
        form = AcoTutoriasForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarTutoria?submitted=True')
        else:
            form = AcoTutoriasForm()
            form.save()
            return HttpResponseRedirect('adicionarTutoria?submitted=True')
    else:
        form = AcoTutoriasForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'acompanhamentos/adicionarTutoria.html', context)

def atualizarTutoria(request, tutoria_id):
    tutoria = get_object_or_404(Acompanhamentos, AsTut_id=tutoria_id)

    form = AcoTutoriasForm(request.POST or None, instance=tutoria)
    if form.is_valid():
        form.save()
        return redirect('acoTutIndex')

    return render(request, 'acompanhamentos/atualizarTutoria.html', {
        'tutoria': tutoria,
        'form': form
    })

def buscarTutoria(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            tutorias = AcompanhamentoTutores.objects.order_by('-AsTut_id').filter(
                Q(AsTut_tutor__icontains=searched) |
                Q(AsTut_acompanhamento__aco_aluno_pcd__alu_nome__icontains=searched) |
                Q(AsTut_acompanhamento__aco_semestre__icontains=searched)
            )
        else:
            tutorias = None

        return render(request, 'acompanhamentos/buscarTutoria.html', {
            'searched': searched,
            'tutorias': tutorias
        })
    else:
        return render(request, 'acompanhamentos/buscarTutoria.html', {

        })

def deletarTutoria(request, tutoria_id):
    tutoria = get_object_or_404(AcompanhamentoTutores, AsTut_id=tutoria_id)
    tutoria.delete()
    return redirect('acoTutIndex')