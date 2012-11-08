from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from django.template import RequestContext

from econ_indicator.forms import HistoryForm
from econ_indicator.models import EconomicIndicator

def home(request):
    ind_id, history = None, None
    if request.method == 'POST':
        ind_id = request.POST.get('indicator')
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(ind_id)
    else:
        form = HistoryForm()

    indicators = EconomicIndicator.objects.all()
    if ind_id:
        heading = EconomicIndicator.objects.get(pk=ind_id)
    else:
        heading = indicators[0]
    return render_to_response('home.html',
                              {'form': form,
                               'heading': heading,
                               'history':history,
                               'indicators': indicators},
                              context_instance=RequestContext(request))

def get_indicator(request):
    ind_id = request.GET.get('indicator')
    indicator = EconomicIndicator.objects.get(pk=int(ind_id))
    data = {'ind_id': indicator.pk, \
            'short_name':indicator.short_name, 'long_name':indicator.long_name}
    json = simplejson.dumps(data)
    return HttpResponse(json, mimetype='application/json')

