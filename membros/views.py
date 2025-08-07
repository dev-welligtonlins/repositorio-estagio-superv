from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import AlunoPcd, Monitor, Tutor, Interprete
from .forms import AlunosForm, MonitoresForm, TutoresForm, InterpretesForm


# Create your views here.
#ADMIN================================================================================================

def admIndex(request):
    return render(request, 'administrador/admIndex.html')

def homologarAtivo(request):
    alunos = AlunoPcd.objects.all().order_by('alu_nome').filter(alu_ativo = True)
    monitores = Monitor.objects.all().order_by('mon_nome').filter(mon_ativo = True)
    tutores = Tutor.objects.all().order_by('tut_nome').filter(tut_ativo = True)
    interpretes = Interprete.objects.all().order_by('int_nome').filter(int_ativo = True)

    return render(request, 'administrador/homologarAtivo.html', {
        'alunos': alunos,
        'monitores': monitores,
        'tutores': tutores,
        'interpretes': interpretes
    })

def homologarInativo(request):
    alunos = AlunoPcd.objects.all().order_by('alu_nome').filter(alu_ativo = False)
    monitores = Monitor.objects.all().order_by('mon_nome').filter(mon_ativo = False)
    tutores = Tutor.objects.all().order_by('tut_nome').filter(tut_ativo = False)
    interpretes = Interprete.objects.all().order_by('int_nome').filter(int_ativo = False)

    return render(request, 'administrador/homologarInativo.html', {
        'alunos': alunos,
        'monitores': monitores,
        'tutores': tutores,
        'interpretes': interpretes
    })

def ativarAluno(request, aluno_id):
    usuario = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    usuario.ativar()
    return redirect('homologarInativo')

def ativarMonitor(request, monitor_id):
    usuario = get_object_or_404(Monitor, mon_id=monitor_id)
    usuario.ativar()
    return redirect('homologarInativo')

def ativarTutor(request, tutor_id):
    usuario = get_object_or_404(Tutor, tut_id=tutor_id)
    usuario.ativar()
    return redirect('homologarInativo')

def ativarInterprete(request, interprete_id):
    usuario = get_object_or_404(Interprete, int_id=interprete_id)
    usuario.ativar()
    return redirect('homologarInativo')
def desativarAluno(request, aluno_id):
    usuario = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    usuario.desativar()
    return redirect('homologarAtivo')

def desativarMonitor(request, monitor_id):
    usuario = get_object_or_404(Monitor, mon_id=monitor_id)
    usuario.desativar()
    return redirect('homologarAtivo')

def desativarTutor(request, tutor_id):
    usuario = get_object_or_404(Tutor, tut_id=tutor_id)
    usuario.desativar()
    return redirect('homologarAtivo')

def desativarInterprete(request, interprete_id):
    usuario = get_object_or_404(Interprete, int_id=interprete_id)
    usuario.desativar()
    return redirect('homologarAtivo')

def homologarAlunoAtivo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    return render(request, 'administrador/homologarAlunoAtivo.html', {
        'aluno': aluno
    })

def homologarAlunoInativo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    return render(request, 'administrador/homologarAlunoInativo.html', {
        'aluno': aluno
    })

def homologarInterpreteAtivo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    return render(request, 'administrador/homologarInterpreteAtivo.html', {
        'interprete': interprete
    })

def homologarInterpreteInativo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    return render(request, 'administrador/homologarInterpreteInativo.html', {
        'interprete': interprete
    })

def homologarMonitorAtivo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    return render(request, 'administrador/homologarMonitorAtivo.html', {
        'monitor': monitor
    })

def homologarMonitorInativo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    return render(request, 'administrador/homologarMonitorInativo.html', {
        'monitor': monitor
    })

def homologarTutorAtivo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    return render(request, 'administrador/homologarTutorAtivo.html', {
        'tutor': tutor
    })

def homologarTutorInativo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    return render(request, 'administrador/homologarTutorInativo.html', {
        'tutor': tutor
    })

def buscarAtivo(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched) | Q(alu_curso__icontains=searched)).filter(alu_ativo=True)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=True)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=True)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=True)
            except:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched)).filter(alu_ativo=True)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=True)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=True)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=True)
        else:
            alunos = None
            monitores = None
            tutores = None
            interpretes = None

        return render(request, 'administrador/buscarAtivo.html', {
            'searched': searched,
            'alunos': alunos,
            'monitores': monitores,
            'tutores': tutores,
            'interpretes': interpretes
        })
    else:
        return render(request, 'administrador/buscarAtivo.html', {

        })

def buscarInativo(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched) | Q(alu_curso__icontains=searched)).filter(alu_ativo=False)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=False)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=False)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=False)
            except:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(
                    Q(alu_nome__icontains=searched)).filter(alu_ativo=False)
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched)).filter(mon_ativo=False)
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched)).filter(tut_ativo=False)
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched)).filter(int_ativo=False)
        else:
            alunos = None
            monitores = None
            tutores = None
            interpretes = None

        return render(request, 'administrador/buscarInativo.html', {
            'searched': searched,
            'alunos': alunos,
            'monitores': monitores,
            'tutores': tutores,
            'interpretes': interpretes
        })
    else:
        return render(request, 'administrador/buscarInativo.html', {

        })

def deletarAlunoAtivo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    aluno.delete()
    return redirect('homologarAtivo')

def deletarAlunoInativo(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    aluno.delete()
    return redirect('homologarInativo')

def deletarMonitorAtivo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    monitor.delete()
    return redirect('homologarAtivo')

def deletarMonitorInativo(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    monitor.delete()
    return redirect('homologarInativo')

def deletarTutorAtivo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    tutor.delete()
    return redirect('homologarAtivo')

def deletarTutorInativo(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    tutor.delete()
    return redirect('homologarInativo')

def deletarInterpreteAtivo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    interprete.delete()
    return redirect('homologarAtivo')

def deletarInterpreteInativo(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    interprete.delete()
    return redirect('homologarInativo')

def adminAlunos(request):
    alunos = AlunoPcd.objects.all().order_by('alu_nome')


    paginator = Paginator(alunos, 10)
    page = request.GET.get('p')
    alunos = paginator.get_page(page)

    return render(request, 'administrador/alunos.html', {
        'alunos': alunos
    })

def adicionarAluno(request):
    submitted = False

    context = {}
    if request.POST:
        form = AlunosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adicionarAluno?submitted=True')
        else:
            form = AlunosForm()
            form.save()
            return HttpResponseRedirect('adicionarAluno?submitted=True')
    else:
        form = AlunosForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'administrador/adicionarAluno.html', context)

# def adicionarAluno(request):
#     submitted = False
#     endSubmitted = False
#
#     context = {}
#     if 'btnAluno' in request.POST:
#         aluForm = AlunosForm(request.POST)
#
#         if aluForm.is_valid():
#             aluForm.save()
#             return HttpResponseRedirect('adicionarAluno?submitted=True')
#         else:
#             aluForm = AlunosForm()
#             aluForm.save()
#             return HttpResponseRedirect('adicionarAluno?submitted=True')
#     elif 'btnEndereco' in request.POST:
#         endForm = EnderecosForm(request.POST)
#         if endForm.is_valid():
#             endForm.save()
#             return HttpResponseRedirect('adicionarAluno?endSubmitted=True')
#         else:
#             endForm = EnderecosForm()
#             endForm.save()
#             return HttpResponseRedirect('adicionarAluno?endSubmitted=True')
#     elif 'endSubmitted' in request.GET:
#         aluForm = AlunosForm
#         endForm = EnderecosForm()
#     else:
#         aluForm = AlunosForm()
#         endForm = EnderecosForm()
#         if 'submitted' in request.GET:
#             submitted = True
#     context['aluForm'] = aluForm
#     context['endForm'] = endForm
#     context['submitted'] = submitted
#     return render(request, 'administrador/adicionarAluno.html', context)

def buscarAluno(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(Q(alu_nome__icontains=searched) | Q(alu_curso__icontains=searched))
            except:
                alunos = AlunoPcd.objects.order_by('alu_nome').filter(Q(alu_nome__icontains=searched))
        else:
            alunos = None

        return render(request, 'administrador/buscarAluno.html', {
            'searched': searched,
            'alunos': alunos
        })
    else:
        return render(request, 'administrador/buscarAluno.html', {

        })


def admAluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    return render(request, 'administrador/admAluno.html', {
        'aluno': aluno
    })

def atualizarAluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    form = AlunosForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('alunos')

    return render(request, 'administrador/atualizarAluno.html', {
        'aluno': aluno,
        'form': form
    })

def deletarAluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    aluno.delete()
    return redirect('alunos')

def adminMonitores(request):
    monitores = Monitor.objects.all().order_by('mon_nome')

    paginator = Paginator(monitores, 10)
    page = request.GET.get('p')
    monitores = paginator.get_page(page)

    return render(request, 'administrador/monitores.html', {
        'monitores': monitores
    })


def adicionarMonitor(request):
    submitted = False

    context = {}
    if request.POST:
        form = MonitoresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adicionarMonitor?submitted=True')
        else:
            form = MonitoresForm()
            form.save()
            return HttpResponseRedirect('adicionarMonitor?submitted=True')
    else:
        form = MonitoresForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'administrador/adicionarMonitor.html', context)


def buscarMonitor(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                monitores = Monitor.objects.order_by('mon_nome').filter(
                    Q(mon_nome__icontains=searched) | Q(mon_curso__icontains=searched))
            except:
                monitores = Monitor.objects.order_by('mon_nome').filter(Q(mon_nome__icontains=searched))
        else:
            monitores = None

        return render(request, 'administrador/buscarMonitor.html', {
            'searched': searched,
            'monitores': monitores
        })
    else:
        return render(request, 'administrador/buscarMonitor.html', {

        })


def admMonitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    return render(request, 'administrador/admMonitor.html', {
        'monitor': monitor
    })


def atualizarMonitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)

    form = MonitoresForm(request.POST or None, instance=monitor)
    if form.is_valid():
        form.save()
        return redirect('monitores')

    return render(request, 'administrador/atualizarMonitor.html', {
        'monitor': monitor,
        'form': form
    })


def deletarMonitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    monitor.delete()
    return redirect('monitores')

def adminTutores(request):
    tutores = Tutor.objects.all().order_by('tut_nome')

    paginator = Paginator(tutores, 10)
    page = request.GET.get('p')
    tutores = paginator.get_page(page)

    return render(request, 'administrador/tutores.html', {
        'tutores': tutores
    })


def adicionarTutor(request):
    submitted = False

    context = {}
    if request.POST:
        form = TutoresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adicionarTutor?submitted=True')
        else:
            form = TutoresForm()
            form.save()
            return HttpResponseRedirect('adicionarTutor?submitted=True')
    else:
        form = TutoresForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'administrador/adicionarTutor.html', context)


def buscarTutor(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                tutores = Tutor.objects.order_by('tut_nome').filter(
                    Q(tut_nome__icontains=searched) | Q(tut_curso__icontains=searched))
            except:
                tutores = Tutor.objects.order_by('tut_nome').filter(Q(tut_nome__icontains=searched))
        else:
            tutores = None

        return render(request, 'administrador/buscarTutor.html', {
            'searched': searched,
            'tutores': tutores
        })
    else:
        return render(request, 'administrador/buscarTutor.html', {

        })


def admTutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    return render(request, 'administrador/admTutor.html', {
        'tutor': tutor
    })


def atualizarTutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)

    form = TutoresForm(request.POST or None, instance=tutor)
    if form.is_valid():
        form.save()
        return redirect('tutores')

    return render(request, 'administrador/atualizarTutor.html', {
        'tutor': tutor,
        'form': form
    })


def deletarTutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    tutor.delete()
    return redirect('tutores')

def adminInterpretes(request):
    interpretes = Interprete.objects.all().order_by('int_nome')

    paginator = Paginator(interpretes, 10)
    page = request.GET.get('p')
    interpretes = paginator.get_page(page)

    return render(request, 'administrador/interpretes.html', {
        'interpretes': interpretes
    })


def adicionarInterprete(request):
    submitted = False

    context = {}
    if request.POST:
        form = InterpretesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adicionarInterprete?submitted=True')
        else:
            form = InterpretesForm()
            form.save()
            return HttpResponseRedirect('adicionarInterprete?submitted=True')
    else:
        form = InterpretesForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'administrador/adicionarInterprete.html', context)


def buscarInterprete(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                interpretes = Interprete.objects.order_by('int_nome').filter(
                    Q(int_nome__icontains=searched) | Q(int_curso__icontains=searched))
            except:
                interpretes = Interprete.objects.order_by('int_nome').filter(Q(int_nome__icontains=searched))
        else:
            interpretes = None

        return render(request, 'administrador/buscarInterprete.html', {
            'searched': searched,
            'interpretes': interpretes
        })
    else:
        return render(request, 'administrador/buscarInterprete.html', {

        })


def admInterprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    return render(request, 'administrador/admInterprete.html', {
        'interprete': interprete
    })


def atualizarInterprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)

    form = InterpretesForm(request.POST or None, instance=interprete)
    if form.is_valid():
        form.save()
        return redirect('interpretes')

    return render(request, 'administrador/atualizarInterprete.html', {
        'interprete': interprete,
        'form': form
    })


def deletarInterprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    interprete.delete()
    return redirect('interpretes')

#ALUNO================================================================================================

def aluIndex(request):
    alunos = AlunoPcd.objects.all()
    paginator = Paginator(alunos, 10)

    page = request.GET.get('p')
    alunos = paginator.get_page(page)

    return render(request, 'alunos/aluIndex.html', {
     'alunos' : alunos
    })

def acompanhantes(request):
    return render(request, 'alunos/acompanhantes.html')

def aluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    return render(request, 'alunos/aluno.html', {
        'aluno' : aluno
    })

#MONITOR_TUTOR========================================================================================

def index_mon(request):
    monitores = Monitor.objects.all()
    paginator = Paginator(monitores, 10)

    page = request.GET.get('p')
    monitores = paginator.get_page(page)
    return render(request, 'monitor_tutor/index_mon.html', {
        'monitores' : monitores
    })

def monAluno(request):
    return render(request, 'monitor_tutor/monAluno.html')

def monitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    return render(request, 'monitor_tutor/monitor.html', {
        'monitor' : monitor
    })

def index_tut(request):
    tutores = Tutor.objects.all()
    paginator = Paginator(tutores, 10)

    page = request.GET.get('p')
    tutores = paginator.get_page(page)
    return render(request, 'monitor_tutor/index_tut.html', {
        'tutores' : tutores
    })

def tutAluno(request):
    return render(request, 'monitor_tutor/tutAluno.html')

def tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    return render(request, 'monitor_tutor/tutor.html', {
        'tutor' : tutor
    })

#INTERPRETE============================================================================================

def intIndex(request):
    interpretes = Interprete.objects.all()
    paginator = Paginator(interpretes, 10)

    page = request.GET.get('p')
    interpretes = paginator.get_page(page)
    return render(request, 'interpretes/intIndex.html', {
        'interpretes' : interpretes
    })

def intAluno(request):
    return render(request, 'interpretes/intAluno.html')

def interprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    return render(request, 'interpretes/interprete.html', {
        'interprete' : interprete
    })

