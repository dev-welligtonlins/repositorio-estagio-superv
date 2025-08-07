from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Feedbacks
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import FeedbacksForm

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
def feeIndex(request):
    feedbacks = Feedbacks.objects.order_by('-fee_id')
    paginator = Paginator(feedbacks, 10)

    page = request.GET.get('p')
    feedbacks = paginator.get_page(page)
    return render(request, 'feedbacks/feeIndex.html', {
        'feedbacks': feedbacks
    })

def adicionarFeedback(request):
    submitted = False

    context = {}
    if request.POST:
        form = FeedbacksForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarFeedback?submitted=True')
        else:
            form = FeedbacksForm()
            form.save()
            return HttpResponseRedirect('adicionarFeedback?submitted=True')
    else:
        form = FeedbacksForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'feedbacks/adicionarFeedback.html', context)

def feedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    return render(request, 'feedbacks/feedback.html', {
        'feedback': feedback
    })

def atualizarFeedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, fee_id=feedback_id)

    form = FeedbacksForm(request.POST or None, instance=feedback)
    if form.is_valid():
        form.save()
        return redirect('feeIndex')

    return render(request, 'feedbacks/atualizarFeedback.html', {
        'feedback': feedback,
        'form': form
    })

def buscarFeedback(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            feedbacks = Feedbacks.objects.order_by('-fee_id').filter(Q(fee_titulo__icontains=searched) | Q(fee_descricao__icontains=searched) )
        else:
            feedbacks = None

        return render(request, 'feedbacks/buscarFeedback.html', {
            'searched': searched,
            'feedbacks': feedbacks
        })
    else:
        return render(request, 'feedbacks/buscarFeedback.html', {

        })
