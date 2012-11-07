from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext

from econ_indicator.forms import HistoryForm
from econ_indicator.models import EconomicIndicator

def home(request):
    historyform = HistoryForm()
    indicators = EconomicIndicator.objects.all()
    return render_to_response('home.html',
                              {'form': historyform,
                               'heading': indicators[0],
                               'indicators': indicators},
                              context_instance=RequestContext(request))


