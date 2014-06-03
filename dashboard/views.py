from django.shortcuts import render, render_to_response, HttpResponseRedirect, redirect
from models import Candidates
from forms import CandidatesForm
from django.template import RequestContext
from django.views.generic import UpdateView, DeleteView
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django_tables2   import RequestConfig
from tables import CandidatesTable

# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    table = CandidatesTable(Candidates.objects.all())
    RequestConfig(request, paginate=False).configure(table)
    return render(request, "dashboard.html", {'table': table})

@login_required(login_url='/login/')
def add(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = CandidatesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            print form.errors
    else:
        form = CandidatesForm()
    return render_to_response('add.html', {'CandidatesForm': CandidatesForm, 'form': form}, context)

class UpdateCandidate(UpdateView):
    model = Candidates
    form_class = CandidatesForm
    template_name = 'update.html'
    success_url = '/dashboard/'

class DeleteCandidate(DeleteView):
    model = Candidates
    template_name = 'delete.html'
    success_url = '/dashboard/'

@login_required(login_url='/login/')
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login/')

def home_page(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    else:
        return redirect('django.contrib.auth.views.login')