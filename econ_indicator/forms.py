from django import forms
from django.forms import ModelForm
from econ_indicator.models import History, EconomicIndicator

class HistoryForm(ModelForm):
    class Meta:
        model = History
        exclude = ['indicator']

    def clean_month(self):
        month = self.cleaned_data['month']
        if int(month) not in range(1,13):
            raise forms.ValidationError("Invalid choice for month")
        return month

    def clean_year(self):
        year = self.cleaned_data['year']
        if int(year) not in range(2000,2013):
            raise forms.ValidationError("Invalid choice for year")
        return year

    def save(self, ind_id, commit=True):
        data = self.cleaned_data
        country = data['country']
        state = data['state']
        year = data['year']
        month = data['month']
        nominal = data['nominal']
        indicator = EconomicIndicator(pk=ind_id)
        history = History(country=country, state=state, year=year,\
                month=month, nominal=nominal, indicator=indicator)
        history.save()
        return history

