from django.shortcuts import render, render_to_response
from models import Candidates
from forms import CandidatesForm
from django.template import RequestContext

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html", {"dashboard": Candidates.objects.all()})

def add(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = CandidatesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return dashboard(request)
        else:
            print form.errors
    else:
        form = CandidatesForm()
    return render_to_response('add.html', {'CandidatesForm': CandidatesForm, 'form': form}, context)