import django_tables2 as tables
from models import Candidates
from django_tables2.utils import A

TEMPLATE = '''
   <a href="{% url 'update_candidate' record.pk %}">Update</a>
   <a href="{% url 'delete_candidate' record.pk %}">Delete</a>
'''

class CandidatesTable(tables.Table):
    column_name = tables.TemplateColumn(TEMPLATE, verbose_name=" ")
    class Meta:
        model = Candidates
        attrs = {"class": "paleblue"}