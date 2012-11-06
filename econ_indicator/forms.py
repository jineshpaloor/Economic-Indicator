from django.forms import ModelForm
from econ_indicator.models import History

class HistoryForm(ModelForm):
    class Meta:
        model = History
