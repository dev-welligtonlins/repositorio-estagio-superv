from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Avisos
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import AvisosForm

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
def aviIndex(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndex.html', {
        'avisos': avisos
    })

def aviIndexAluno(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexAluno.html', {
        'avisos': avisos
    })

def adicionarAviso(request):
    submitted = False

    context = {}
    if request.POST:
        form = AvisosForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarAviso?submitted=True')
        else:
            form = AvisosForm()
            form.save()
            return HttpResponseRedirect('adicionarAviso?submitted=True')
    else:
        form = AvisosForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'avisos/adicionarAviso.html', context)

def buscarAviso(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAviso.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAviso.html', {

        })

def aviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/aviso.html', {
        'aviso': aviso
    })

def atualizarAviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    form = AvisosForm(request.POST or None, instance=aviso)
    if form.is_valid():
        form.save()
        return redirect('aviIndex')

    return render(request, 'avisos/atualizarAviso.html', {
        'aviso': aviso,
        'form': form
    })

def deletarAviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    aviso.delete()
    return redirect('aviIndex')



#ALUNO

def aviIndexAluno(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexAluno.html', {
        'avisos': avisos
    })

def avisoAluno(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoAluno.html', {
        'aviso': aviso
    })


def buscarAvisoAluno(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAvisoAluno.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAvisoAluno.html', {

        })

def avisoAluno(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoAluno.html', {
        'aviso': aviso
    })
