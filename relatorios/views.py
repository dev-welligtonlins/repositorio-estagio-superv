from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import RelatoriosMon, RelatoriosTut
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import RelatoriosMonForm, RelatoriosTutForm

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
def relMIndex(request):
    relatoriosM = RelatoriosMon.objects.order_by('-relM_id')
    paginator = Paginator(relatoriosM, 10)

    page = request.GET.get('p')
    relatoriosM = paginator.get_page(page)
    return render(request, 'relatorios/relMIndex.html', {
        'relatoriosM': relatoriosM
    })

def relTIndex(request):
    relatoriosT = RelatoriosTut.objects.order_by('-relT_id')
    paginator = Paginator(relatoriosT, 10)

    page = request.GET.get('p')
    relatoriosT = paginator.get_page(page)
    return render(request, 'relatorios/relTIndex.html', {
        'relatoriosT': relatoriosT
    })

def adicionarRelatorioM(request):
    submitted = False

    context = {}
    if request.POST:
        form = RelatoriosMonForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarRelatorioM?submitted=True')
        else:
            form = RelatoriosMonForm()
            form.save()
            return HttpResponseRedirect('adicionarRelatorioM?submitted=True')
    else:
        form = RelatoriosMonForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'relatorios/adicionarRelatorioM.html', context)

def adicionarRelatorioT(request):
    submitted = False

    context = {}
    if request.POST:
        form = RelatoriosTutForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarRelatorioT?submitted=True')
        else:
            form = RelatoriosTutForm()
            form.save()
            return HttpResponseRedirect('adicionarRelatorioT?submitted=True')
    else:
        form = RelatoriosTutForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'relatorios/adicionarRelatorioT.html', context)

def relatorioM(request, relatorioM_id):
    relatorioM = get_object_or_404(RelatoriosMon, relM_id=relatorioM_id)

    return render(request, 'relatorios/relatorioM.html', {
        'relatorioM': relatorioM
    })

def relatorioT(request, relatorioT_id):
    relatorioT = get_object_or_404(RelatoriosTut, relT_id=relatorioT_id)

    return render(request, 'relatorios/relatorioT.html', {
        'relatorioT': relatorioT
    })

def atualizarRelatorioM(request, relatorioM_id):
    relatorioM = get_object_or_404(RelatoriosMon, relM_id=relatorioM_id)

    form = RelatoriosMonForm(request.POST or None, instance=relatorioM)
    if form.is_valid():
        form.save()
        return redirect('relMIndex')

    return render(request, 'relatorios/atualizarRelatorioM.html', {
        'relatorioM': relatorioM,
        'form': form
    })

def atualizarRelatorioT(request, relatorioT_id):
    relatorioT = get_object_or_404(RelatoriosTut, relT_id=relatorioT_id)

    form = RelatoriosTutForm(request.POST or None, instance=relatorioT)
    if form.is_valid():
        form.save()
        return redirect('relTIndex')

    return render(request, 'relatorios/atualizarRelatorioT.html', {
        'relatorioT': relatorioT,
        'form': form
    })

def buscarRelatorioM(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            relatoriosM = RelatoriosMon.objects.order_by('-relM_id').filter(Q(relM_titulo__icontains=searched))
        else:
            relatoriosM = None

        return render(request, 'relatorios/buscarRelatorioM.html', {
            'searched': searched,
            'relatoriosM': relatoriosM
        })
    else:
        return render(request, 'relatorios/buscarRelatorioM.html', {

        })

def buscarRelatorioT(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            relatoriosT = RelatoriosTut.objects.order_by('-relT_id').filter(Q(relT_titulo__icontains=searched))
        else:
            relatoriosT = None

        return render(request, 'relatorios/buscarRelatorioT.html', {
            'searched': searched,
            'relatoriosT': relatoriosT
        })
    else:
        return render(request, 'relatorios/buscarRelatorioT.html', {

        })