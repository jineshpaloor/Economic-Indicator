from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
from econ_indicator.forms import HistoryForm

def home(request):
    historyform = HistoryForm()
    return render_to_response('home.html',
                              {'form': historyform},
                              context_instance=RequestContext(request))


