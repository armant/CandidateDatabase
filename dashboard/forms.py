from django import forms
from models import Candidates

class CandidatesForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = ('first_name', 'last_name', 'birth_date', 'nationality', 'level_of_english', 'note', 'resume', )