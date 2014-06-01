from django.shortcuts import render
from models import Candidates

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html", {"dashboard": Candidates.objects.all()})